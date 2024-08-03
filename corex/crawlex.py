import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore
import concurrent.futures
import os
import threading
from concurrent.futures import ThreadPoolExecutor

# Lock for thread-safe URL set operations
visited_urls_lock = threading.Lock()

def extract_urls(soup, base_url):
    """
    Extracts all URLs from the provided BeautifulSoup object that are within the same domain as the base URL.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object containing HTML content.
        base_url (str): The base URL to resolve relative URLs.

    Returns:
        set: A set of absolute URLs within the same domain.
    """
    
    urls = set()
    tags = ['a', 'link', 'img', 'script', 'iframe', 'form']
    attributes = ['href', 'src', 'action']
    
    for tag in tags:
        elements = soup.find_all(tag)
        for element in elements:
            for attribute in attributes:
                url = element.get(attribute)
                if url:
                    full_url = urljoin(base_url, url)
                    if urlparse(full_url).netloc == urlparse(base_url).netloc:
                        urls.add(full_url)
    return urls

def contains_xxe_indicators(body):
    """
    Checks if the response body contains indicators of XML External Entity (XXE) vulnerability.

    Parameters:
        body (str): The response body to check.

    Returns:
        bool: True if XXE indicators are found, False otherwise.
    """
    body_lower = body.lower()
    if 'xml' in body_lower and 'parser' in body_lower and 'error' in body_lower:
        xml_index = body_lower.find('xml')
        parser_index = body_lower.find('parser')
        error_index = body_lower.find('error')
        if xml_index < parser_index < error_index:
            return True
    return False


def fetch_url(url, headers=None, body=None, session=None):
    """
    Fetches the content of a URL and returns the response, or None if there is a request exception.

    Parameters:
        url (str): The URL to fetch.
        headers (dict): Optional HTTP headers to include in the request.
        body (str): Optional body data to include in the request (typically not used in GET requests).

    Returns:
        tuple: A tuple containing:
            - response (Response or None): The HTTP response object if the request was successful, otherwise None.
            - url (str): The URL that was fetched.
    """
    try:
        response = session.get(url, headers=headers, data=body) if session else requests.get(url, headers=headers, data=body)
        return response
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def crawl(url, max_depth=1, current_depth=0, visited_urls=None, headers=None, body=None, session=None):
    """
    Crawls a URL recursively up to a specified depth and checks for XXE indicators.

    Parameters:
        url (str): The starting URL to crawl.
        max_depth (int): The maximum depth of recursion.
        current_depth (int): The current recursion depth.
        visited_urls (set): Set of URLs that have been visited.
        headers (dict): Optional headers to include in requests.
        body (str): Optional body to include in requests.

    Returns:
        tuple: A tuple containing:
            - set: A set of URLs where XXE indicators were found.
            - set: A set of all visited URLs.
    """
    
    if visited_urls is None:
        visited_urls = set()

    if current_depth > max_depth or url in visited_urls:
        return set(), visited_urls

    visited_urls.add(url)
    xml_urls = set()

    response = fetch_url(url, headers, body, session)
    if not response:
        return xml_urls, visited_urls

    if contains_xxe_indicators(response.text):
        print(f"Possible XML data transfer detected at: {Fore.GREEN}{url}{Fore.RESET}")
        xml_urls.add(url)

    soup = BeautifulSoup(response.text, 'lxml')  # Use 'html.parser' for HTML content
    urls = extract_urls(soup, url)

    # Limiting max_workers to avoid overload
    max_workers = min(32, os.cpu_count() + 4)  

    # Crawl found URLs using multithreading
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(crawl, u, max_depth, current_depth + 1, visited_urls, headers, body, session): u for u in urls if u not in visited_urls}

        for future in concurrent.futures.as_completed(future_to_url):
            u = future_to_url[future]
            try:
                found_xml_urls, updated_visited_urls = future.result()
                xml_urls.update(found_xml_urls)
                visited_urls.update(updated_visited_urls)
            except Exception as e:
                print(f"Exception occurred while crawling {u}: {e}")

    return xml_urls, visited_urls

def check_xxe(url, headers=None, body=None):
    """
    Performs a POST request to the specified URL and checks for XXE indicators in the response.

    Parameters:
        url (str): The URL to send the POST request to.
        headers (dict): Optional headers to include in the request.
        body (str): Optional body to include in the request.

    Returns:
        None
    """
    try:
        headers = headers or {}
        headers['Content-Type'] = 'application/xml'
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            headers['Host'] = parsed_url.netloc
        if body:
            headers['Content-Length'] = str(len(body))

        response = requests.post(url, headers=headers, data=body)

        if contains_xxe_indicators(response.text):
            print(f"Possible XML data transfer detected at: {Fore.GREEN} {url} {Fore.RESET}")
            #print(f"Response: {response.text}")

    except requests.RequestException as e:
        print(f"Request failed: {e}")


