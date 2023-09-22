from googlesearch import search

from smtplib import SMTP, SMTPRecipientsRefused, SMTPSenderRefused, SMTPResponseException
from email.mime.multipart import MIMEMultipart
import re
import os
import time
import requests
import ipaddress
from colorama import *
from time import sleep
import sys
import json
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
from pathlib import Path
import platform
from datetime import datetime
import phonenumbers
import folium
from bs4 import BeautifulSoup as bs
#29 modules

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
WHITE = "\033[0;37m"

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

banner = ("""
▒██   ██▒ ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▒▒ █ █ ▒░▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
░░  █   ░▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
 ░ █ █ ▒ ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██▒ ▒██▒░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
▒▒ ░ ░▓ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
░░   ░▒ ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
 ░    ░  ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
 ░    ░      ░ ░        ░   ░           ░          
   An Open Source Intelligence Framework                          
        Created by: AnonyminHack5
        Team: TermuxHackz Society
        	Version: \033[1;92m2.1\033[0m
	   \033[1;97mPlatform: \033[0m\033[1;96m""" + platform.system())


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)


main_menu = ("""
	\033[1;91m[??] Choose an option:
	\033[1;91m[\033[1;33;40m1\033[0m\033[1;91m] \033[1;97m IP Address Information
	\033[1;91m[\033[1;33;40m2\033[0m\033[1;91m] \033[1;97m Email Address Information \033[1;91m[\033[1;92mNOT WORKING FOR NOW!\033[0m\033[1;91m]
	\033[1;91m[\033[1;33;40m3\033[0m\033[1;91m] \033[1;97m Phone Number Information  \033[1;91m[\033[1;92mNOT WORKING FOR NOW!\033[0m\033[1;91m]
	\033[1;91m[\033[1;33;40m4\033[0m\033[1;91m] \033[1;97m Host Search
	\033[1;91m[\033[1;33;40m5\033[0m\033[1;91m] \033[1;97m Ports
	\033[1;91m[\033[1;33;40m6\033[0m\033[1;91m] \033[1;97m Exploit CVE
	\033[1;91m[\033[1;33;40m7\033[0m\033[1;91m] \033[1;97m Exploit Open Source Vulnerability Database 
	\033[1;91m[\033[1;33;40m8\033[0m\033[1;91m] \033[1;97m DNS Lookup
	\033[1;91m[\033[1;33;40m9\033[0m\033[1;91m] \033[1;97m DNS Reverse
        \033[1;91m[\033[1;33;40m10\033[0m\033[1;91m] \033[1;97mEmail Finder
        \033[1;91m[\033[1;33;40m11\033[0m\033[1;91m] \033[1;97mExtract Metadata from image
        \033[1;91m[\033[1;33;40m12\033[0m\033[1;91m]\033[1;97m Check Twitter Status
        \033[1;91m[\033[1;33;40m13\033[0m\033[1;91m]\033[1;97m Subdomain Enumeration
        \033[1;91m[\033[1;33;40m14\033[0m\033[1;91m]\033[1;97m Google Dork Hacking
        \033[1;91m[\033[1;33;40m15\033[0m\033[1;91m]\033[1;97m SMTP Analysis
        \033[1;91m[\033[1;33;40mNULL\033[0m\033[1;91m]\033[1;97m Movie Database OSINT
        \033[1;91m[\033[1;33;40m17\033[0m\033[1;91m]\033[1;97m Dark Web Search
        \033[1;91m[\033[1;33;40m18\033[0m\033[1;91m]\033[1;97m Next
        \033[1;91m[\033[1;33;40m19\033[0m\033[1;91m]\033[1;97m Report bugs
	\033[1;91m[\033[1;33;40m99\033[0m\033[1;91m]\033[1;97m Update X-osint
	\033[1;91m[\033[1;33;40m100\033[0m\033[1;91m]\033[1;97m About
	\033[1;91m[\033[1;33;40m00\033[0m\033[1;91m]\033[1;97m Quit
	
	""")


about = """\033[1;90m
This is an osint tool which gathers useful and yet credible valid information about a phone number, user email address and ip address, \nVIN, Protonmail account and so much more, X-osint is an Open source intelligence framework, \nfeel free to clone this repo, if you have features you would like to add or any fixes please open an issue or create a merge
\033[0m"""
def traceip():
	targetip = input("\033[1;91mEnter IP Address: \033[0m")
	r = requests.get("http://ip-api.com/json/" + targetip)
	print("\n\033[1;91m[*]\033[1;97m IP detail is given down below\n")
	#print()
	sleep(0.1)
	print("\033[1;92m \033[1;91m➤\033[1;97m Status Code    : " + str(r.status_code))
	sleep(0.1)
	if str(r.json() ['status']) == 'success':
		print(" \033[1;91m➤\033[1;97m Status         :\033[1;92m " + str(r.json() ['status']))
		sleep(0.1)
	elif str(r.json() ['status']) == 'fail':
		print(" \033[1;91m➤\033[1;97m Status         :\033[1;97m " + str(r.json() ['status']) + '\033[1;92m')
		sleep(0.1)
		print(" \033[1;91m➤\033[1;97m Message        : " + str(r.json() ['message']))
		sleep(0.1)
		if str(r.json() ['message']) == 'invalid query':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is an invalid IP Address, So you can try another IP Address.\n')
			exit()
		elif str(r.json() ['message']) == 'private range':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a private IP Address, So This IP can not be traced.\n')
			exit()
		elif str(r.json() ['message']) == 'reserved range':
			print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a reserved IP Address, So This IP can not be traced.\n')
			exit()
		else:
			print('\nCheck your internet connection.\n')
			exit()
	print("\033[1;92m \033[1;91m➤\033[1;97m Target IP      : " + str(r.json() ['query'] ))
	sleep(0.1)
	print("\033[1;92m \033[1;91m➤\033[1;97m Country:	: " + str(r.json() ['country'] ))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m Country Code    : " + str(r.json() ['countryCode']))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m City   	: " + str(r.json() ['city']))
	sleep(0.1)
	print(" \033[1;92m\033[1;97m➤\033[1;97m Timezone    	: " + str(r.json() ['timezone']))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Region Name    : " + str(r.json() ['regionName'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Region         : " + str(r.json() ['region'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m ZIP Code       : " + str(r.json() ['zip'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Latitude       : " + str(r.json() ['lat'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Longitude      : " + str(r.json() ['lon'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m ISP            : " + str(r.json() ['isp'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Organization   : " + str(r.json() ['org'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m AS             : " + str(r.json() ['as'] ))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Location       : " + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print(" \033[1;91m➤\033[1;97m Google Map     : \033[1;94mhttps://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
	sleep(0.1)
	print()
	mapaddress = input("\033[1;91m[*]\033[1;97m Press ENTER To Open Location on Google maps or press any other key to quit: ")
	if mapaddress == "":
		print()
		print("[*] Opening Location on google map")
		print()
		os.system("xdg-open https://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']) + " > /dev/null 2>&1")
		print()
	else:
		print()
		print("[*] Aborting.....")
		print()

###email address information gathering
def email_info():
	mailid = input("\033[1;91m Enter email address: \033[1;94m")
	if not re.match(r"[^@]+@[^@]+\.[^@]+", mailid):
		print("Please input a valid Email Address!")
		return
	eml = requests.get("https://ipqualityscore.com/api/json/email/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mailid)
	if str(eml.json()['success']) == "False":
		print(eml.json()['message'])
		return
	print()
	sleep(1)
	print()
	print("\033[1;91m[~]\033[1;97m E-mail Details are given down below")
	print()
	print("\033[1;91m➤\033[1;97m Target E-mail       : " + str(mailid) )
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Status Code         : " + str(eml.status_code) )
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Valid               : " + str(eml.json() ['valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Catch All           : " + str(eml.json() ['catch_all']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Common              : " + str(eml.json() ['common']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Deliverability      : " + str(eml.json() ['deliverability']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Disposable          : " + str(eml.json() ['disposable']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m DNS Valid           : " + str(eml.json() ['dns_valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Fraud Score         : " + str(eml.json() ['fraud_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Frequent Complainer : " + str(eml.json() ['frequent_complainer']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Generic             : " + str(eml.json() ['generic']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Honeypot            : " + str(eml.json() ['honeypot']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Leaked              : " + str(eml.json() ['leaked']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Message             : " + str(eml.json() ['message']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Over All Score      : " + str(eml.json() ['overall_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Recent Abuse        : " + str(eml.json() ['recent_abuse']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Request ID          : " + str(eml.json() ['request_id']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Sanitized E-mail    : " + str(eml.json() ['sanitized_email']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMTP Score          : " + str(eml.json() ['smtp_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Spam Trap Score     : " + str(eml.json() ['spam_trap_score']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Success             : " + str(eml.json() ['success']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Suggested Domain    : " + str(eml.json() ['suggested_domain']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Suspect             : " + str(eml.json() ['suspect']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Timed Out           : " + str(eml.json() ['timed_out']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m First Name          : " + str(eml.json() ['first_name']))
	sleep(0.1)
	print()
	print("\033[1;91m[~]\033[1;94m Domain Age")
	print()
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['domain_age'] ['human']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['domain_age'] ['iso']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['domain_age'] ['timestamp']))
	sleep(0.1)
	print()
	print("\033[1;91m[~]\033[1;94m First Seen")
	print()
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['first_seen'] ['human']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['first_seen'] ['iso']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['first_seen'] ['timestamp']))
	sleep(0.1)
	print()
 
 ### Phone number info
def phone_info():
	mobileno = input("\033[1;91m [+]\033[1;92m Enter phone number with country code: \033[1;97m")
	try:
		parse = phonenumbers.parse(mobileno)
	except:
		print('\033[1;91m[!]\033[1;97mPlease add "+" sign to the country code\033[0m\n')
		time.sleep(1)
		phone_info()
	if phonenumbers.is_valid_number(parse) is False:
		print(Fore.RED + "[!]" + Fore.WHITE + "You have just entered an invalid phone number!!dammit!!\n")
		time.sleep(1)
		phone_info()
	from phonenumbers import geocoder
	pepnumber = phonenumbers.parse(mobileno)
	location = geocoder.description_for_number(pepnumber, 'en')
	#print(location)
	from opencage.geocoder import OpenCageGeocode
	
	if os.path.exists("./opencage_api.txt") and os.path.getsize("./opencage_api.txt") > 0:
		with open('opencage_api.txt', 'r') as file:
			opencage_api=file.readline().rstrip('\n')

	else:
		file = open("opencage_api.txt", "w")
		opencage_api = input("""\n[+] Please enter a valid Opencage API key (Get from opencagedata.com): """)
		file.write(opencage_api)
		print("[+] File written: ./opencage_api.txt")
		file.close()
	key = opencage_api ##I may change this and replace it with a tempporary API
	#API_KEY
	geocoder = OpenCageGeocode(key)
	query = str(location)
	results = geocoder.geocode(query)
      
	phe = requests.get("https://ipqualityscore.com/api/json/phone/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mobileno )
	sleep(1)
	print()
	time.sleep(3)
	print("\033[1;97mIf you get an error it is likely due to the number of request going into the server so try again later\033[0m")
	print()
	print("\033[1;91m[~]\033[1;97m Phone Number Details are given down below")
	print()
	print("\033[1;91m➤\033[1;97m Target Number  : " + mobileno)
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Status Code    : " + str(phe.status_code))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Valid          : " + str(phe.json() ['valid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m VOIP           : " + str(phe.json() ['VOIP']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Active         : " + str(phe.json() ['active']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Active Status  : " + str(phe.json() ['active_status']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Carrier        : " + str(phe.json() ['carrier']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m City           : " + str(phe.json() ['city']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Country        : " + str(phe.json() ['country']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Dialing Code   : " + str(phe.json() ['dialing_code']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Line Type      : " + str(phe.json() ['line_type']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Local Format   : " + str(phe.json() ['local_format']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m MCC            : " + str(phe.json() ['mcc']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Name           : " + str(phe.json() ['name']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Prepaid        : " + str(phe.json() ['prepaid']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMS Domain     : " + str(phe.json() ['sms_domain']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m SMS E-mail     : " + str(phe.json() ['sms_email']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Spammer        : " + str(phe.json() ['spammer']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Success        : " + str(phe.json() ['success']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m TimeZone       : " + str(phe.json() ['timezone']))
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Zip Code       : " + str(phe.json() ['zip_code']))
	sleep(0.1)
	print()
	print("\033[1;91m➤\033[1;97m Success        : " + str(phe.json() ['success']))
	sleep(0.1)
	print()
	print("\033[1;91m➤\033[1;97m VIP INFO \033[0m")
	sleep(0.1)
	#print(results) #printresult from geocoder
	
	lat = results[0]['geometry']['lat']
	lng = results[0]['geometry']['lng']
	
	
	print('\033[1;91m➤\033[1;97m Location: ', lat, lng)
	myMap = folium.Map(location=[lat, lng], zoom_start=9)
	folium.Marker([lat, lng], popup=location).add_to(myMap)
	
	##Save the html newly generated file
	myMap.save("target_location.html")
 
	open_result = input("""\n Do you want to open result in your brower? [Y] or [N]: """)
 
	if open_result == "Y" or "y":
		try:
			os.system("xdg-open target_location.html")
			time.sleep(1)
			sys.exit(1)
		except KeyboardInterrupt:
			print('CTRL C Detected..Quitting')
			exit()
	elif open_result == "N" or "n":
		sys.exit(1)

#### Update script
def update():
	os.system("clear")
	print(banner)
	print()
	print("\033[1;91m➤\033[1;97m Searching for updates...-> \033[0m\033[1;94mFound")
	sleep(0.1)
	print("\033[1;91m➤\033[1;97m Updating.. \033[0m")
	sleep(0.1)
	print()
	print()
	print("\033[1;91m\tSelect your terminal for update \033[0m\n")
	print("\033[1;91m\t[!] PLEASE MAKE SURE YOU CHOOSE CORRECTLY [!] \033[0m\n\n")
	print("\033[1;34m\t\t[\033[0m\033[1;77m1\033[0m\033[1;34m]\033[0m\033[1;93mTermux\033[0m")
	print("\033[1;34m\t\t[\033[0m\033[1;77m2\033[0m\033[1;34m]\033[0m\033[1;93mLinux\033[0m\n")
	update_terminal = input("\033[1;94mChoose: \033[0m")
	
	if update_terminal == "1":
		print("\033[1;97m[+] Updating for termux......\033[0m")
		print()
		sleep(0.1)
		os.system("cd $HOME")
		os.system("cd $PREFIX/bin && rm xosint")
		print("\033[1;97m[+] Validating installation....\033[0m\n")
		sleep(0.1)
		path_to_file = '/$PREFIX/bin/xosint'
		path = Path(path_to_file)
		if path.is_file():
			print(f'The file {path_to_file} exists, Validation failed, Kindly update manually')
			time.sleep(1)
			exit()
		else:
			print(f'The file {path_to_file} doesnt exists, Validation Successful')
			time.sleep(0.5)
			print("\033[1;91m[!]\033[0m\033[1;97mAutomatic update Completed\0330m\n")
			time.sleep(0.9)
			os.system("cd $HOME")
			os.system("git clone https://github.com/TermuxHackz/X-osint")
			print("\033[1;97m[+] Granting permissions.....\033[0m\n")
			os.system("cd $HOME && cd X-osint")
			os.system("chmod +x *")
			sleep(0.5)
			print("\033[1;97m[+] Preparing Setup file.....\033[0m\n")
			sleep(0.5)
			print("\033[1;97m[+] Setup file ready!!.....Starting in 2s...\033[0m\n")
			print("\033[1;97m[+] Update completed.....\033[0m\n")
			sleep(2)
			os.system("cd $HOME ")
			os.system("cd X-osint && bash setup.sh")

			

	elif update_terminal == "2":
		print("\033[1;97m[+] Updating for linux......\033[0m")
		print()
		sleep(0.1)
		os.system("cd $HOME")
		os.system("cd /usr/local/bin && sudo rm xosint")
		print("\033[1;97m[+] Validating installation....\033[0m\n")
		sleep(0.5)
		path_to_file = '/usr/local/bin/xosint'
		path = Path(path_to_file)
		if path.is_file():
			print(f'The file {path_to_file} exists, Validation failed, Kindly update manually')
			time.sleep(1)
			exit()
		else:
			os.system("cd $HOME")
			os.system("git clone https://github.com/TermuxHackz/X-osint")
			print("")
			print("\033[1;97m[+] Granting permissions.....\033[0m\n")
			os.system("cd X-osint")
			os.system("sudo chmod +x *")
			sleep(0.5)
			print("\033[1;97m[+] Preparing Setup file.....\033[0m\n")
			sleep(0.5)
			print("\033[1;97m[+] Setup file ready!!.....Starting in 2s...\033[0m\n")
			print("\033[1;97m[+] Update completed.....\033[0m\n")
			sleep(2)
			os.system("cd $HOME")
			os.system("cd X-osint && bash setup.sh")
	else:
		print("Invalid input....KINDLY UPDATE...quiting..")
		sleep(0.5)
		exit
		
#### STart main script
### 4, 5, 6, 7
os.system("clear")
print(banner)
print(main_menu)
option = input("\033[1;91mxosint>> \033[1;97m") 
if option == "1":
	traceip()
elif option == "2":
	email_info()
elif option == "3":
	phone_info()
elif option == "4":
	def shodan_host():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		host_ip = input("\033[1;91m[+]\033[0m\033[1;97mShodan Host Search (IP): \033[0m")
		url = "https://api.shodan.io/shodan/host/"+ host_ip +"?key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_host()
elif option == "5":
	def shodan_ports():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		url = "https://api.shodan.io/shodan/ports?key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_ports()
elif option == "6":
	def shodan_exploit_cve():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		exploit_cve = input("\033[1;91m[+]\033[0m\033[1;97mExploit CVE: \033[0m")
		url = "https://exploits.shodan.io/api/search?query="+ "cve:" + exploit_cve +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_exploit_cve()
elif option == "7":
	def shodan_exploit_osvdb():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		exploit_osvdb = input("\033[1;91m[+]\033[0m\033[1;97mExploit Open Source Vulnerability Database: \033[0m")
		url = "https://exploits.shodan.io/api/search?query="+ "osvdb:" + exploit_osvdb +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_exploit_osvdb()
	
elif option == "8":
	def shodan_dns_lookup():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		hostnames = input("\033[1;91m[+]\033[0m\033[1;97mDNS Lookup: \033[0m")
		url = "https://api.shodan.io/dns/resolve?hostnames="+ hostnames +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_dns_lookup()
	
elif option == "9":
	def shodan_dns_reverse():
		if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
			with open('api.txt', 'r') as file:
				shodan_api=file.readline().rstrip('\n')
		else:
			file = open('api.txt', 'w')
			shodan_api = input("[+] Please enter a valid Shodan API key (Shodan.io): ")
			file.write(shodan_api)
			print("[+] File written: ./api.txt")
			file.close()
		ips = input("\033[1;91m[+]\033[0m\033[1;97mDNS Reverse: \033[0m")
		url = "https://api.shodan.io/dns/reverse?ips="+ ips +"&key=" + shodan_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))
	shodan_dns_reverse()

elif option == "10":
	def hunter_email_finder():
		email_domain = input("\033[1;91m[+]\033[0m\033[1;97mDomain: \033[0m")
		first_name = input("\033[1;91m[+]\033[0m\033[1;97mFirst Name: \033[0m")
		last_name = input("\033[1;91m[+]\033[0m\033[1;97mLast Name: \033[0m")
		url = "https://api.hunter.io/v2/email-finder?domain="+ email_domain + "&first_name=" + first_name +"&last_name=" + last_name +"&api_key=" + hunter_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))

	if os.path.exists("./hunter_io_api.txt") and os.path.getsize("./hunter_io_api.txt") > 0:
		with open('hunter_io_api.txt', 'r') as file:
			hunter_api=file.readline().rstrip('\n')
	else:
		file = open('hunter_io_api', 'w')
		hunter_api = input("[+] Please enter a valid Hunter API key to continue (Get from Hunter.io): ")
		file.write(hunter_api)
		print("[+] File written: ./hunter_io_api.txt")
		file.close()
		hunter_email_finder()

	def hunter_email_finder():
		email_domain = input("\033[1;91m[+]\033[0m\033[1;97mDomain: \033[0m")
		first_name = input("\033[1;91m[+]\033[0m\033[1;97mFirst Name: \033[0m")
		last_name = input("\033[1;91m[+]\033[0m\033[1;97mLast Name: \033[0m")
		url = "https://api.hunter.io/v2/email-finder?domain="+ email_domain + "&first_name=" + first_name +"&last_name=" + last_name +"&api_key=" + hunter_api
		request = requests.get(url)
		txt = request.text
		parsed = json.loads(txt)
		print(json.dumps(parsed, indent=2, sort_keys=True))

elif option == "11":
	print("\033[1;91m[!]NOTICE:\033[0m\033[1;93m To get a better metadata of the image please do not use images from whatsapp or social media platforms as they strip away metadata from images, also do not use screenshot images, USE IMAGES TAKEN FROM A DEVICE CAMERA THANK YOU [!]\033[0m")
	print()
	imagename = input("\033[1;91m[+]\033[0m\033[1;97m Enter Correct path of the image (JPEG ONLY): \033[0m")
	print("")
	print()
	# open the image
	exif_dict = piexif.load(imagename)
	print(f'Metadata for {imagename}:')
	for ifd in exif_dict:
		print(f'{ifd}:')
		for tag in exif_dict[ifd]:
			tag_name = piexif.TAGS[ifd][tag]["name"]
			tag_value = exif_dict[ifd][tag]
			
			if isinstance(tag_value, bytes):
				tag_value = tag_value[:10]
			print(f'\t{tag_name:25}: {tag_value}')
	print()

		
elif option == "12":
	email_add = input("\033[1;91m[+]\033[0m\033[1;97mEnter email: \033[0m")
	url = "https://api.twitter.com/i/users/email_available.json?email=" + email_add 
	request = requests.get(url)
	txt = request.text
	parsed = json.loads(txt)
	print(json.dumps(parsed, indent=2, sort_keys=True))
			
elif option == "13":
	print("DOESN'T WORKING")
#### Google Dorking Hacking 

elif option == "14":
		try:
			## print_formatted_text(HTML('<b><u>;GOOGLE DORK HACKING </u></b>')) 
			dork = input('\033[1;91m\n[+]\033[0m\033[1;97mEnter The Dork Search Query (eg: intext:"Index of /" +passwd): \033[0m')
			amount = input("\033[1;91m[+]\033[0m\033[1;97mEnter The Number Of sites To dork (eg: 4): \033[0m")
			print ("\n ")
			
			requ = 0
			counter = 0
			
			for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
				counter = counter + 1
				print ("[+] ", counter, results)
				time.sleep(0.1)
				requ += 1
				if requ >= int(amount):
					break
				data = (counter, results)
				time.sleep(0.1)
				print("\n")
			file = input('\033[1;91m[!]\033[0m\033[1;94mEnter name to save output as (eg: output.txt): \033[0m')
			original_stdout = sys.stdout
			try:
				with open(file, 'w') as f:
					sys.stdout = f
					print(data)
					print("\n")
					sys.stdout = original_stdout
					print("\033[1;97m[+]\033[0mFile has been saved as \033[0m" + file)
			except:
				print("\033[1;91m[!]Please enter a name to save the file as [!]\033[0m")
				sys.exit(1)

		except KeyboardInterrupt:
			print ("\n")
			print ("\033[1;91m[!] User Interruption Detected..!\033[0")
			time.sleep(0.5)
			print ("[•] Done... Exiting...")
			sys.exit(1)
			
elif option == "19":
	print("\033[1;91m[+]\033[1;97m Kindly take a screenshot or screenrecord of the error faced and mail them \nto me and i would give you feedback based on those bugs you have \nreported to me and fix them, Thank you \033[0m")
	print("")
	try:
		report = input('\033[1;95mReport bug (y/n): \033[0m')
		if report == "y":
			try:
				import webbrowser
				webbrowser.open('mailto:?to=AnonyminHack5@protonmail.com&subject=X-osint-bugs', new=1)
			except ImportError:
				print("\033[1;91m[!] Webbrowser module not found!!, Install using \033[0m\033[1;97mpip install webbrowser\033[0m")
				print("[+] Try reporting bugs again ")
				time.sleep(0.9)
				sys.exit(1)
		elif report == "n":
			print("[+] Seems there wasnt any bugs for you to report, so why bother choosing to report bugs, lol ")
			time.sleep(0.5)
			sys.exit(1)
		else:
			print("\033[1;91m[!] Invalid Command!!!\033[0m")
			time.sleep(0.1)
			sys.exit(1)
	except KeyboardInterrupt:
		print ("\n")
		print ("\033[1;91m[!] User Interruption Detected..!\033[0")
		time.sleep(0.5)
		sys.exit(1)
elif option == "15":
	def spoof(target,ports):
		TestedPorts = []
		if ("ports"=="*"):
			TestedPorts = ['25','465','587','2525']
			ports = "25, 465, 587 and 2525"
		else:
			TestedPorts = list(ports.split(","))
			testuser = "testuser@mail.ca"
			message = MIMEMultipart()
			message["From"] = testuser
			message["To"] = testuser
			message["Subject"] = "test"
			text = message.as_string()
			print("\033[1;91m{}[!]\033[0m\033[1;97mLooking For Email Spooffing Vulnerability on port {}..... \033[0m\033[1;91m[!]\033[0m\n\033[94m".format(WHITE,ports))
			for port in TestedPorts: 
				print("{} Testing Email Spoofing on port {}.....\n\033[94m".format(WHITE,port))
			try:
				SMTP(target,port).sendmail(testuser,testuser,text)
				print("{} The SMTP Server Targeted : {} is potentialy vulnerable to mail spoofing. Authentification don't seem to be required on port {} \033[0;37m \n".format(GREEN,target,port))
			except (SMTPRecipientsRefused, SMTPSenderRefused, SMTPResponseException):
				print("{} Recipient error encountered. The SMTP Server Targeted: {} don't seem to be vunlerable to mail spoofing on port {} \033[0;37m \n ".format(BLUE,target,port))
			except ConnectionRefusedError:
				print("{} Connection refused by host {}. It don't seem to be vunlerable to mail spoofing on port {} \033[0;37m \n".format(BLUE,target,port))
			except Exception:
				print("{} Exception Occured on host {}. It don't seem to be vunlerable to mail spoofing on port {} \033[0;37m \n".format(BLUE,target,port))
			except KeyboardInterrupt:
				print("Stopping...")
				exit()
	def userenum (target,ports):
		TestedPorts = []
		if (ports =="*"):
			TestedPorts = ['25','465','587','2525']
			ports = "25, 465, 587 and 2525"
		else:
			TestedPorts = list(ports.split(","))
			print("\033[1;91m{}[!]\033[0m\033[1;97m Looking For user enumeration vulnerability on port {}..... \033[0m\n\033[94m".format(WHITE,ports))
		for port in TestedPorts:
			print("\033[1;91m{}[!]\033[0m\033[1;997m Testing user enumeration on port {}.....\033[0m\n\033[94m".format(WHITE,port))
		try:
			verify = SMTP(target, port).verify("")
			if verify[0] in [250, 252]:
				print("{} The SMTP Server Targeted: {} is potentialy vulnerable to user enumeration on port {}. VRFY query responded status : {}  \033[0;37m \n".format(GREEN,target,port,verify[0]))
			else:
				print("{} The SMTP Server Targeted: {} don't seem to be vulberable to user enumeration on port {}. VRFY query responded statys : {}  \033[0;37m \n".format(BLUE,target,port,verify[0]))
		except Exception:
			print("{} Exception Occured on host {}. It don't seem to be vunlerable to user enumeration on port {}. \033[0;37m \n".format(BLUE,target,port))
		except KeyboardInterrupt:
			print("Stopping...")
			exit()

	target = input("\033[1;91m[+]\033[0m\033[1;97mEnter SMTP Server: \033[0m")
	port = input('\033[1;91m[+]\033[0m\033[1;97mEnter port or type "*" to use all ports: \033[0m')
	spoof(target,port)
	userenum(target,port)

#### DEEP WEB SCRAPING OSINT

elif option == "17":
	W = '\033[0m'
	C = '\033[36m'
	R = '\033[31m'
	G = '\033[32m'
	
	try:
		import subprocess as subp
	except ImportError:
		print("Required Module not installed...exiting")
		exit()

	def service():
		print('\n' + C + "[~]Checking for tor service...." + W + '\n')
		if platform.system() == "Linux":
			cmd = 'systemctl is-active tor.service && tor'
			co = subp.Popen(cmd, shell=True,stdout=subp.PIPE).communicate()[0]
			if 'inactive' in str(co):
				print(R + '[!] Tor Service is not Running ' + W + '\n')
				print(R + '[!] Tor Service is required to Run this feature... ')
				print(R + '[!] Type' + W + " tor " + R + 'if your using termux or type' + W + " service tor start " + R + 'if your using linux\n')
				print(C + '[*] After doing that run ' + W + " xosint " + C + 'again ') 
				exit()
			else:
				print(C + '[+] Tor Service is running....' + W + '\n')
		else:
			command = "tor"
			os.system(command)
			print(C + '[+] Tor Service is running...' + W + '\n')

	def scrap():
		r = "http://icanhazip.com"
		page = requests.get(r)
		print(R + '[+]' + G + ' Connected to Tor....')
		print(R + '[->]' + G + 'Your tor ip --> ' + page.text)
	
	
	def main():
		from bs4 import BeautifulSoup
		
		session = requests.session()
		#session.proxies["http"] = "127.0.0.1:9050" 
		#session.proxies["https"] = "127.0.0.1:9050"
		
		
		query = input('\033[1;91m[+]\033[0m\033[1;94mEnter keyword to search: \033[0m')
		URL = f"https://ahmia.fi/search/?q={query}"
		page = requests.get(URL)
		request = requests.get(URL)
		
		if request.status_code == 200:
			print('\n' + G + '[!] Request went through \n')
			time.sleep(0.5)
			print(G + '[+] Getting .onion links for you: [+] \033[0m\n')
			time.sleep(0.5)
			soup = BeautifulSoup(page.content, "html.parser")
			for a_href in soup.find_all("a", href=True):
				print(a_href["href"])
			time.sleep(0.5)
			choice = input('\033[1;91m[+]\033[0m\033[1;94mOpen results in browser? (y/n): \033[0m')
			if choice == "y":
				import webbrowser
				webbrowser.open(f"https://ahmia.fi/search/?q={query}")
				time.sleep(0.5)
				print("If it doesnt open, its most likely your using Termux")
			elif choice == "n":
				sys.exit(1)
			else:
				print("Wrong input")
				exit()
		else:
			print(R + '[!] Request didnt go through please check your network or try again later \n')
			exit(1)
	service()
	scrap()
	main()

elif option == "18":
    os.system("clear")
    print(banner)
    second_main_menu = ("""
                     \033[1;91m[??] Choose an option:
                     \033[1;91m[\033[1;33;40m18\033[0m\033[1;91m] \033[1;97m Protonmail OSINT
                     \033[1;91m[\033[1;33;40m19\033[0m\033[1;91m] \033[1;97m Vehicle Identification Number OSINT
                     \033[1;91m[\033[1;33;40m20\033[0m\033[1;91m] \033[1;97m Basic Github OSINT
                     \033[1;91m[\033[1;33;40m21\033[0m\033[1;91m] \033[1;97m Vehicle License plate OSINT \033[1;91m[\033[0m\033[1;96mUNDER DEVELOPMENT\033[0m\033[1;91m]\033[0m
                     \033[1;91m[\033[1;33;40mG\033[0m\033[1;91m] \033[1;97m  Go back
                     """) ##I would still add more here
    print(second_main_menu)
    second_input = input('\033[1;91mxosint>> \033[0m')

    if second_input == "18":
        def extract_timestamp(mail, source_code):
            try:
                timestamp = re.sub(':', '', re.search(':[0-9]{10}::', source_code.text)[0])
                return datetime.frontimestamp(int(timestamp))
            except AttributeError:
                return None
        # CHecks if its a business mail address
        
        # Protonmail account validity check
        def protonmailaccountcheck():
            invalidEmail = True
            regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
            print("\n\nYou want to know if a protonmail email is real or not?")
            while invalidEmail:
                mail = input("\033[1;91m[+]\033[1;97m Enter the email(protonmail accounts only!!): \033[0m")
                print("")
                if(re.search(regexEmail,mail)):
                    invalidEmail = False
                else:
                    print("Invalid Email")
                    invalidEmail = True
            #Check if the protonmail exist : valid / not valid
            requestProton = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search='+str(mail))
            bodyResponse = requestProton.text
            protonNoExist = "info:1:0" #not valid
            protonExist = "info:1:1" #valid
            if protonNoExist in bodyResponse:
                print("\033[1;91m[!]\033[0m\033[1;97m Protonmail email is \033[0m" + f"{bcolors.FAIL}not valid{bcolors.ENDC}")
            if protonExist in bodyResponse:
                print("\033[1;91m[+]\033[0m\033[1;97m Protonmail email is \033[0m" + f"{bcolors.OKGREEN}valid{bcolors.ENDC}")
                regexPattern1 = "2048:(.*)::" #RSA 2048-bit (Older but faster)
                regexPattern2 = "4096:(.*)::" #RSA 4096-bit (Secure but slow)
                regexPattern3 = "22::(.*)::" #X25519 (Modern, fastest, secure)
            try:
                timestamp = int(re.search(regexPattern1, bodyResponse).group(1))
                dtObject = datetime.fromtimestamp(timestamp)
                print("")
                print("\033[1;91m[+]\033[0m\033[1;97m Date and time of the creation:\033[0m", dtObject)
                print("")
                print("\033[1;91m[+]\033[0m\033[1;97m Encryption : RSA 2048-bit (Older but faster)\033[0m")
            except:
                try:
                    timestamp = int(re.search(regexPattern2, bodyResponse).group(1))
                    dtObject = datetime.fromtimestamp(timestamp)
                    print("\033[1;91m[+]\033[0m\033[1;97m Date and time of the creation:\033[0m\n", dtObject)
                    print("\033[1;91m[+]\033[0m\033[1;97m Encryption : RSA 4096-bit (Secure but slow)\033[0m")
                except:
                    timestamp = int(re.search(regexPattern3, bodyResponse).group(1))
                    dtObject = datetime.fromtimestamp(timestamp)
                    print("\033[1;91m[+]\033[0m\033[1;97m Date and time of the creation:\033[0m", dtObject)
                    print("\033[1;91m[+]\033[0m\033[1;97m Encryption : X25519 (Modern, fastest, secure)\033[0m")
            #Download the public key attached to the email
            invalidResponse = True
            print("\n\033[1;91m[?]\033[0m\033[1;97mDo you want to download the public key attached to the email ?\033[0m")
            while invalidResponse:
                #Input
                responseFromUser = input("""Please enter "yes" or "no": """)
                #Text if the input is valid
                if responseFromUser == "yes":
                    invalidResponse = False
                    requestProtonPublicKey = requests.get('https://api.protonmail.ch/pks/lookup?op=get&search='+str(mail))
                    bodyResponsePublicKey = requestProtonPublicKey.text
                    print(bodyResponsePublicKey)
                elif responseFromUser == "no":
                    invalidResponse = False
                else:
                    print("Invalid Input")
                    invalidResponse = True

        #Email Search OSINT footprint
        def emailtraces():
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
                AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36'}
            
            print("Checking Server Status\n")
            response = requests.get('https://google.com', headers)
            print(response)
            if response.status_code == 200:
                print("Status: \033[1;94mSuccess!\033[0m\n")
            elif response.status_code == 404:
                print("\033[1;91m404 Not Found, please try again!!\033[0m")
            
            searchfor = input("""\033[1;91m[+]\033[0m\033[1;94m Enter email with quotation marks eg "test@protonmail.com":  \n\033[0m""")
            
            print("\nprocessing request....\n")
            
            for result in search(searchfor, tld="com", stop=10, pause=2):
                print(result)
        
        def check_domain_name(mail):
            return mail.split("@")[1] not in ["protonmail.com", "proton.me"]


        def make_api_request(mail):
            try:
                request = requests.get("https://account.proton.me/api/users/available", 
                                       headers={
                "x-pm-appversion":"web-account@5.0.11.11",
                "x-pm-locale":"en_US"
                },
                params={
                "Name":mail,
                "ParseDomain":"1"})
                is_business_address = check_domain_name(mail) #Return code 429 = API limit exceeded
                
                if (request.status_code == 409):
                    source_code = requests.get(f'https://api.protonmail.ch/pks/lookup?op=index&search={mail}')
                    creation_date = extract_timestamp(mail, source_code)
                    print("\033[1m\n\nProtonMail Account is VALID! Creation date: " + str(creation_date) + " \033[0m\U0001F4A5")
                    return True
                elif(request.status_code == 429):
                    print("\u001b[31m\n\nAPI requests limit exceeded...")
                
                elif is_business_address:
                    print("\u001b[33m\nProtonmail API does not handle business emails, ""but you can get account creation date + PGP Key")
                    return True
                else:
                    print("\u001b[31m\n\nProtonMail account is NOT VALID")
                    return False
            except:
                print("Error when requesting the API")
                return False

        
        
        #Get protonmail user PGP key
        def pgpkeyinformation():
            choice = input("""
                 View PGP key in Terminal  [T] or Download Key [D]: """)
            
            if choice == "T" or "t":
                pgpkeyview()
            if choice == "D" or "d":
                pgpkeydirectdownload()
                
        def pgpkeydirectdownload():
            email_query = input("\nEnter target email to download PGP key: ")
            import webbrowser
            alink = 'https://api/protonmail.ch/pks/lookup?op=get&search='+email_query
            new = 2
            webbrowser.open(alink, new=new)
            
        #extract the key
        def extract_key(source_code):
            regex = ':[0-9]{2,4}:(.*)::'
            
            try:
                return re.search(regex, source_code.text)[0].split(":")[1]
            except AttributeError:
                return None
        
        # view pgp key within terminal
        def pgpkeyview():
            invalidEmail = True
            regexEmail = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
            
            print("\nInput protonmail user email to get user's PGP key\n")
            while invalidEmail:
                mail = input("Type in protonmail: ")
                
                if (re.search(regexEmail, mail)):
                    invalidEmail = False
                else:
                    print("Protonmail user doesnt exists\n")
                    invalidEmail = True
            if(make_api_request(mail)):
                source_code = request.get("https://api.protonmail.ch/pks/lookup?op=index&search=" + mail)
                if("info:1.0" in source_code.text):
                    print("Cant get the PGP information")
                else:
                    timestamp = extract_timestamp(mail, source_code)
                    key = extract_key(source_code)
                    
                    print("PGP Key Date and Creation Time: ", str(timestamp))
                    
                    if(key != "22"):
                        print("Encryption Standard: RSA " + key + "-bit")
                    else:
                        print("Encryption standard: ECC Curve")
                    
                    invalidResponse = True
                    
                    print("Get user PGP Key?: ")
                    while invalidResponse:
                        responseFromUser = input("""[Y] or [N]: """)
                        
                        if responseFromUser == "Y":
                            invalidResponse = False
                            requestProtonPublicKey = request.get("https://api.protonmail.ch/pks/lookup?op=index&search=" + str(mail))
                            
                            bodyResponsePublicKey = requestProtonPublicKey.text
                            print(bodyResponsePublicKey)
                        elif responseFromUser == "N":
                            invalidResponse
                        else:
                            print("Input not valid")
                            invalidResponse = True
        #CHeck user Ip belongs to protonVPN user       
        def protonvpnipsearch():
            while True:
                try:
                    ip = ipaddress.ip_address(input('Enter IP Address: '))
                    
                    break
                except ValueError:
                    continue
            requestProton_vpn = requests.get("https://api.protonmail.ch/vpn/logicals")
            bodyResponse = requestProton_vpn.text
            if str(ip) in bodyResponse:
                print("\033[1;92m[+] This Ip is currently associated to protonVPN \033[0m")
            else:
                print("\033[1;91m[!] This Ip is not associated with any protonVPN Account\033[0m")
                
        def checkProtonAPIStatut():
            requestProton_mail_statut = requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=test@protonmail.com')
            if requestProton_mail_statut.status_code == 200:
                print("Protonmail API is " + f"{bcolors.BOLD}ONLINE{bcolors.ENDC}")
            else:
                print("Protonmail API is " + f"{bcolors.BOLD}OFFLINE{bcolors.ENDC}")
                requestProton_vpn_statut = requests.get('https://api.protonmail.ch/vpn/logicals')
                if requestProton_vpn_statut.status_code == 2:
                    print("Protonmail VPN is " + f"{bcolors.BOLD}ONLINE{bcolors.ENDC}")
                else:
                    print("Protonmail VPN is " + f"{bcolors.BOLD}OFFLINE{bcolors.ENDC}")

        
        proton_osint = ("""
                      \033[1;91m[\033[1;33;40m1\033[0m\033[1;91m] \033[1;97m Protonmail Account Check
                      \033[1;91m[\033[1;33;40m2\033[0m\033[1;91m] \033[1;97m Email Traces
                      \033[1;91m[\033[1;33;40m3\033[0m\033[1;91m] \033[1;97m ProtonVPN IP Search
                      \033[1;91m[\033[1;33;40m4\033[0m\033[1;91m] \033[1;97m PGP Key Information
                      \033[1;91m[\033[1;33;40mG\033[0m\033[1;91m] \033[1;97m Go back
                      """)
        print(proton_osint)
        b_osint = input('\033[1;91m[+]\033[0m\033[1;94m Make your choice: \033[0m')
        checkProtonAPIStatut()
        if b_osint == "1":
            ##checkprotonmailapistatus()
            protonmailaccountcheck()
      
        elif b_osint == "2":
            emailtraces()
        elif b_osint == "3":
            protonvpnipsearch()
        elif b_osint == "4":
            pgpkeyinformation()
        elif b_osint == "G" or "g":
            os.system("cd $HOME")
            os.system("sudo xosint || xosint")
        else:
            print("\033[1;91m[!]\033[0m\033[1;97mInvalid Command..exiting\033[0m")
            time.sleep(0.0001)
            exit()
    elif second_input == "19":
        open_terminal = ("""
                      \033[1;91m[\033[1;33;40m1\033[0m\033[1;91m] \033[1;97m View in CLI
                      \033[1;91m[\033[1;33;40m2\033[0m\033[1;91m] \033[1;97m View in GUI
                      \033[1;91m[\033[1;33;40mG\033[0m\033[1;91m] \033[1;97m Go back
                      """)
        print(open_terminal)
        c_input = input('\033[1;91m[+]\033[0m\033[1;94m Make your choice: \033[0m')
        
        if c_input == "1":
            #import vininfo
            import click
            from vininfo import Vin
            num = input("\033[1;91m[+]\033[1;97m Enter VIN Number: \033[0m")
            def check(num):
                if Vin(num).verify_checksum():
                    click.secho('Checksum is valid', fg='green')
                else:
                    click.secho('Checksum is not valid', fg='red', err=True)
                    sys.exit(1)
            check(num)
            vin = Vin(num)
            
            print("")
            click.secho('Basic:')
            print("\033[1;97m[+] Country: \033[0m" + vin.country)
            print()
            time.sleep(0.5)
            print('\033[1;97m[+] Manufacturer: \033[0m' + vin.manufacturer)
            time.sleep(0.5)
            print("\033[1;97m[+] Region: \033[0m" + vin.region)
            time.sleep(0.5)
            print("\033[1;97m[+] Serial: \033[0m" + vin.vis)
            print()
            time.sleep(0.5)
            print('\033[1;97m[+] Plant: \033[0m' + vin.vds)
            time.sleep(0.5)
            print("\033[1;97m[+] Model: \033[0m" + vin.wmi)
            time.sleep(0.5)
            print("")
            click.secho('Year Model')
            print(vin.years)
            print()
            
         
        elif c_input == "2":
            from tkinter import *
            from tkinter import messagebox
            from vininfo import Vin
            import requests
            
            root = Tk()
            
            root.title("X-osint VIN Number Extractor")
            
            #Create a label
            
            lbl_vin_number = Label(root, text="VIN Number:")
            
            lbl_vin_number.grid(row=0, column=0, padx=5, pady=5)
            
            #Create an entry box
            
            ent_vin_number = Entry(root)
            ent_vin_number.grid(row=0, column=1, padx=5, pady=5)
            #Create a button
            btn_extract = Button(root, text="Extract", command=lambda: extract_data(ent_vin_number.get()))
            
            btn_extract.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
            
            def extract_data(vin_number):
                if vin_number == "":
                    messagebox.showinfo("Error", "Please enter a valid VIN number!")
                else:
                    try:
                        vin_url = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesExtended/" + vin_number + "?format=json"
                        vin_data = requests.get(vin_url).json()
                        make = vin_data['Results'][0]['Make']
                        model = vin_data['Results'][0]['Model']
                        year = vin_data['Results'][0]['ModelYear']
                        #country = vin_data['Results'][0]['Country']
                        messagebox.showinfo("VIN Information", "Make: " + make + "\nModel: " + model + "\nYear: " + year)
                    except:
                        messagebox.showinfo("Error", "Invalid VIN number!")
                        
                        #Run the main loop
            root.mainloop()        
                    
            #print("Still in development")
        
        
        elif c_input == "G" or "g":
            os.system("cd $HOME")
            os.system("sudo xosint || xosint")
        else:
            print("\033[1;91m[!]\033[0m\033[1;97mInvalid Command..exiting\033[0m")
            time.sleep(0.0001)
            exit()
    elif second_input == "20":
        import requests
        import find_github_email
        
        username = input("\033[1;91m[+]\033[0m\033[1;97m Enter the Github Username: \033[0m")
        url_link = f'https://api.github.com/users/{username}'
        url_link2 = f'https://api.github.com/users/{username}/repos'
        
        response = requests.get(url_link)
        response1 = requests.get(url_link2)
        
        
        if response.status_code == 200:
            user_data = response.json()
            repos = response1.json()
            
            print(f"\n\033[1;96m Name: \033[0m{user_data['name']}\n")
            print(f"\033[1;96m Location: \033[0m{user_data['location']}\n")
            print(f"\033[1;96m Followers: \033[0m{user_data['followers']}\n")
            print(f"\033[1;96m Following: \033[0m{user_data['following']}\n")
            print(f"\033[1;96m Email Address: \033[0m{user_data['email']}\n")
            print(f"\033[1;96m Number of Repos: \033[0m{len(repos)}\n")
            
            response2 = find_github_email.find(username)
            print(f"\n{response2}\n")
        else:
            print("\n\033[1;97m[!]\033[0m\033[1;91m Error!!!, Couldnt get details, too many requests, \n\033[1;97m Try again after some time!.. \033[0m\n")
            time.sleep(2)
            sys.exit(1)
        
    elif second_input == "21":
        try:
            license_plate = input("\033[1;91m[+]\033[0m\033[1;97m License plate(US License plates ONLY FOR NOW): \033[0m")
            
            lplate = license_plate.upper()
            plate = "".join(license_plate.split(" "))
            
            state = input("\033[1;91m[+]\033[1;97m State (Eg If its Alabama type 'AL'): \033[0m")
            state = state.upper()
            
            print("")
            print("\n\033[1;93mSearching.....\033[0m")
            URL = "https://findbyplate.com/US/"+state+"/"+plate+"/"
            
            page = requests.get(URL, verify=True)
            soupPage = bs(page.content, 'html.parser')
            mayresults = soupPage.find("h2", {"class": "vehicle-modal"})
            mayraw = mayresults.prettify().split("\n")[1]
            may = mayraw[1:len(mayraw)]
            
            year = may[0:4]
            model = may[5:len(may)]
            
            countryResults = soupPage.find("div", {"data-title": "PlantCountry"})
            countryResultsraw = countryResults.prettify().split("\n")[1]
            
            country = countryResultsraw[1:len(countryResultsraw)]
            countryResults = soupPage.find("div", {"data-title": "PlantCity"})
            
            countryResultsraw = countryResults.prettify().split("\n")[1]
            city = countryResultsraw[1:len(countryResultsraw)]
            
            vtypeResults = soupPage.find("div", {"data-title": "VehicleType"})
            
            vtyperaw = vtypeResults.prettify().split("\n")[1]
            type = vtyperaw[1:len(vtyperaw)]
            
            location = city + ", " + country
            
            print("\033[1;92mDone!\033[0m\n")
            
            print("\033[1mModel:\033[0m              \033[1mYear:\033[0m" + " " * 7 + "\033[1mVehicle Type:\033[0m")
            print(model + " " * (20 - len(model)) + year + "        " + type)
            
            print("\n\033[1mPlate Number:\033[0m       \033[1mState:\033[0m      \033[1mPlant Location:\033[0m")
            print(lplate + " " * (20 - len(lplate)) + state + "          " + location)

        except KeyboardInterrupt:
            print("\n\033[91mExiting...\033[0m")
        
        except AttributeError:
            print("\033[1;91mOops!! Vehicle Not Found\033[0m")
        except:
            print("\033[91mError Found, please contact developer\033[0m")
            raise;

        
    
    elif second_input == "G" or "g":
        os.system("cd $HOME")
        os.system("sudo xosint || xosint")

elif option == "99":
	update()
elif option == "00":
	print()
	exit
elif option == "100":
	print(about)
	exit


### ADD NEXT MAIN MENU TO IT
	

else:
	print()
	print("[*] Invalid Input..try again....")
	sleep(0.9)
	exit()
#END OF SCRIPT
