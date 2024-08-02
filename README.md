# eXelion

<p align="center">
    <pre>
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
    </pre>
</p>
<br/>

# Table of Content
- [eXelion](#eXelion)
  * [Description](#Description)
  * [General Informations](#GeneralInformations)
  * [Usage](#Usage)
  * [Features Overview](#FeaturesOverviewt)
  * [Comming soon](#Commingsoon)
  * [Installation](#Installation)
  * [Disclaimer](#Disclaimer)


## Description

eXeleion is a simple tool designed to inject XXE payloads and display the results directly in the terminal.</br>
It can also be used to crawl your target URL and search for all XML data interactions.</br>
Additionally, you can customize your request headers and body to send to your URL and observe the response.</br>

🔧 This tool is still a work in progress, and changes may be implemented as development continues</br>


## General Informations
The tool will always show your request and response for your target </br>
For the following options `-he, -b, -x, -c` you must use the single qutoes '' to customs your Header and Body/XXE Payload </br>
`python3 eXelion.py -he 'header: header' -b 'Body is there' -u http://google.com`</br>

![image](https://github.com/user-attachments/assets/41ba3704-21fb-4f40-8296-746791cc7700)
</br>
</br>



Use the `-st` option to display all available templates. Subsequently, you can customize variables such as the protocol and paths.</br>
`python3 eXelion.py -xlfi -vfp '/tmp/test.txt' -vp 'htpp'`</br>
![image](https://github.com/user-attachments/assets/2a1afa5b-08c1-4c53-a076-1f989a69b119)

</br>
</br>

To search for XML interactions, use the `-cr` option. Additionally, you can view all URLs identified without XML interactions by using the `-crv` option.</br>
`python3 eXelion.py -crv -u https://0a2a006c04b11c5881400c75008b0050.web-security-academy.net/`</br>
![image](https://github.com/user-attachments/assets/00027aee-9f79-4597-b88a-29fceaea3c1d)



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
📤 Customize your own request.</br>
📑 Input your own XXE payloads or load an XML file containing your payloads.</br>
📝 Use and customize the XXE templates.</br>
🔎 Search a website for XML interactions.</br>
 

## Comming soon
⚙️ Pip install features</br>
⚙️ Improve tool performance</br>
⚙️ Function to fuzz the variable in the templates</br>
⚙️ Function to Create a SVG data with XXE Payload</br>
⚙️ Function to create a extern dtd data</br>
⚙️ Function for XML injection</br>
⚙️ Function for XPATH Injection</br>



## Installation

Install eXelion:

```install
git clone https://github.com/K3res/eXelion.git
cd eXelion
pip3 install -r requirements.txt
```



## Disclaimer
This project, including the hacking tool, was developed solely to enhance my coding skills. Users of this tool are fully responsible for any consequences arising from its use.
