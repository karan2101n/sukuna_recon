#!/usr/bin/python3
import os
import requests
import webbrowser

print('''
@author: Sukuna
''')

print("""
<=====================PASSIVE DNSRECON==============================>
[1] wafw00f
[2] nslookup
[3] host
[4] traceroute
[5] dig
[6] whois
[7] netcraft
[8] dnsrecon
[9] all
""")

user = str(input("[+] Enter tool no: "))
target = str(input("[+] Enter Target: "))


def waf():
    print("Checking For Firewall...")
    try:
        os.system(f"wafw00f {target}")
    except:
        print("This tool is not install")
        os.system("sudo apt install wafw00f")

def nslookup():
    print("Checking for nameserver...")
    try:
        os.system(f"nslookup -query=mx -type=txt {target}")
    except:
        print("This tool is not install")
        os.system("sudo apt install nslookup")

def host():
    print("Checking For Host...")
    try:
        os.system(f"host {target}")
    except Error:
        print("This tool is not available")
        os.system("sudo apt install host")

def trace():
    print("Checking routes...")
    try:
        os.system(f"traceroute {target}")
    except error:
        print("Something wents wrong!")

def dig():
    print("Digging...")
    try:
        os.system(f"dig {target} -q-type a,any,mx,ns,soa,hinfo,axfr,txt")
    except:
        print("Something Wents Wrong!")

def whois():
    print("doing whois...")
    try:
        os.system(f"whois {target}")
    except:
        print("Something Wents Wrong!")

def netcraft():
    print("opening netcraft...")
    BaseUrl = "https://sitereport.netcraft.com/?url="
    url = BaseUrl + "https://" + target
    response = requests.get(url)
    web = webbrowser.get('firefox')
    web.open(url)

def dnsrecon():
    print("Dnsrecon...")
    try:
        os.system(f"dnsrecon -d {target}")
    except:
        print("Something wents wrong...")
if user == "1":
    waf()

elif user == "2":
    nslookup()

elif user == "3":
    host()

elif user == "4":
    trace()

elif user == "5":
    dig()
elif user == "6":
    whois()

elif user == "7":
    netcraft()

elif user == "8":
    dnsrecon()
elif user == "9":
    print("<==========================================WAF TESTING==========================================>")
    waf()
    print("<==========================================NSLOOKUP==========================================>")
    nslookup()
    print("<==========================================HOST==========================================>")
    host()
    print("<==========================================TRACROUTE==========================================>")
    trace()
    print("<==========================================DIG==========================================>")
    dig()
    print("<==========================================WHOIS==========================================>")
    whois()
    print("<==========================================NETCRAFT==========================================>")
    netcraft()
    print("<==========================================DNSRECOM==========================================>")
    dnsrecon()
else:
    print("INVALID_INPUT => hasta la vista")
