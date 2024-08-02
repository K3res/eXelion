# eXelion

```
        __   __         _   _                 
        \ \ / /        | | (_)                
   ___   \ V /    ___  | |  _    ___    _ __  
  / _ \   > <    / _ \ | | | |  / _ \  | '_ \ 
 |  __/  / . \  |  __/ | | | | | (_) | | | | |
  \___| /_/ \_\  \___| |_| |_|  \___/  |_| |_|
                      
    
    Version: 0.5 
            
    Author:               K3res
    Github:               https://github.com/K3res/
    Check it Out!:        https://github.com/B0lg0r0v/     
                    

```
<br/>

# Table of Content
- [eXelion](#eXelion)
  * [Description](#Description)
  * [Usage](#Usage)
  * [Features Overview](#FeaturesOverviewt)
  * [Comming soon](#Commingsoon)
  * [Installation](#Installation)
  * [Disclaimer](#Disclaimer)
  * [test](#test)

## Description

eXeleion is a simple tool designed to inject XXE payloads and display the results directly in the terminal.<\br>
It can also be used to crawl your target URL and search for all XML data interactions.<\br>
Additionally, you can customize your request headers and body to send to your URL and observe the response.<\br>

🔧 This tool is still a work in progress, and changes may be implemented as development continues<\br>


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
  -cr, --crawlex        search on the website for XML interaction
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
Customize your own request.<\br>
Input your own XXE payloads or load an XML file containing your payloads.<\br>
Use and customize the XXE templates.<\br>
You can search a website for XML interactions.<\br>
 

## Comming soon
⚙️ Pip install features<\br> 
⚙️ Function to fuzz the variable in the templates</br>
⚙️ Function to Create a SVG data with XXE Payload</br>
⚙️ Function to create a extern dtd data</br>
⚙️ Function for XML injection</br>
⚙️ Function for XPATH Injection</br>



## Installation

You can install this package using pip:

```install
pip install eXelion
```


## Disclaimer
This project, including the hacking tool, was developed solely to enhance my coding skills. Users of this tool are fully responsible for any consequences arising from its use.
