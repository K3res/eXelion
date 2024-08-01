# eXelion

 
![grafik](https://github.com/user-attachments/assets/42668cbc-aeb2-4209-8c07-a0cf693011cb)<br/>

A tool for testing XXE payloads. 



# Table of Content
- [PassGenGo](#eXelion)
  * [Remarks](#test)
  * [Usage](#test)
  * [Examples](#test)
  * [Installation](#test)
  * [Disclaimer](#test)

## Description

eXeleion is a simple tool to inject XXE Payloads and give the result in the terminal back.
It can be also use to crawl your URL Target to search all XML data interactions.  
You can also custom your request Header and body to send it to your URL and see the response. 

🔧 This tool is still a work in progress, and changes may be implemented as development continues

## General Information
- normal function expplain
- Template function explain
  all options
- Crawler function explain

## Usage
```

usage: eXelion.py [options]

Tools for XXE/XEE Payloads

options:
  -h, --help            show this help message and exit

Request options:
  -u URL, --url URL     The URL target http://example.com/XML
  -he HEADERS, --headers HEADERS
                        Use custom headers
  -c COOKIE, --cookie COOKIE
                        Use custom cookie
  -b BODY, --body BODY  Use custom body
  -x XXE, --xxe XXE     Use custom XXE payload
  -xf XXEFILE, --xxefile XXEFILE
                        Use custom XML file with XXE payload

Special options:
  -cr, --crawlex        search on the website for XML
  -crv, --crawlexverbose
                        display all crawled URLs, even if no XML was found
  -t, --time            give the finish time back

Templates options:
  -st, --showTemplates  show all availible templates
  -xfd, --xxeFileDisclosure
                        Use a XXE template to read a file (default value= /etc/shadow)
  -xebl, --xeeBillionLaughs
                        Use the Billion laughs template(DoS attack)
  -xlfi, --xxeLocalFileInclusion
                        Use a XXE template to read a file (default value= /etc/shadow, with LFI)
  -xblfi, --xxeBlindLocalFileInclusion
                        Use a XXE template to read a file (default value= /etc/shadow, with Blind LFI)
  -xacb, --xxeAccessControlBypass
                        Use a XXE bypass to read a PHP file
  -xs, --xxeSSRF        Use a XXE template with a SSRF

Variable Templates Options:
  -vfp VARIABLEFILEPATH, --variableFilePath VARIABLEFILEPATH
                        Variable to change the file path with the file path
  -ve VARIABLEENTITY, --variableEntity VARIABLEENTITY
                        Variable to change the entity name
  -vp VARIABLEPROTOCOL, --variableProtocol VARIABLEPROTOCOL
                        Varaible to change the protocol type
  -vsu VARIABLESSRF, --variableSSRF VARIABLESSRF
                        Varaible to change the URL for SSRF attacks
  -vulfi VARIABLEURLLFI, --variableUrlLFI VARIABLEURLLFI
                        Varaible to change the URL for LFI attacks
 ```                                                                      

 

## Features Overview


## Comming soon
- Function to fuzz the variable in the templates
- Function to Create a SVG data with XXE Payload
- Function to create a extern dtd data
- Function for XML injection
- Function for XPATH Injection



## Installation

You can install this package using pip:

```install
pip install eXelion
```


## Disclaimer
This tool was primarily created as a project to improve my coding skills and begin developing some hacking tools. It is not intended to be the most efficient tool available.
Additionally, you are responsible for any consequences that may arise from using this tool.
