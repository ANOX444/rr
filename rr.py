import requests, os, re, time, random
from keep_alive import keep_alive
from requests.exceptions import RequestException
from time import sleep
import datetime
import os

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
clear()
	    	
def sendcomment():
                count = 0
                while True:
                	try:
                		for line in lines:
                			parameters = {'access_token': access_token, 'message': line}
                			url = "https://graph.facebook.com/v15.0/{0}/".format(cuid)
                			sendmessage = requests.post(url, data=parameters, headers=headers)
                			print("Messege Sent Done ::- ", line, '\')
                			time.sleep(t)
                	except RequestException:
                			print("[×] Error Connection.............\")
                			time.sleep(5.5)       			
               			               			               			
try:
	print("Enter your token file :\If you have not saved file typ 'N'\")
	c = str(input())
	with open(c, 'r') as O:
		access_token = O.read()
		
except:
	print("\You have not saved any token file.\Enter id name of which you want to save token as text file :\")
	tn = str(input())
	print("\Enter your token here :\")
	data = ' '
	f = open(""+ str(tn) + ".txt", "w")
	f.write(data)
	f.close()
	with open(""+ str(tn) + ".txt", 'r') as O:
		access_token = O.read()

print("Entet Conversation Id Here :\")
print(47*'\033[1;35;40m-')
cuid = 't_' + str(cid)
print("\Enter time delay in seconds :\")
t = (5)
sp("\033[1m\033[36m[?] Enter Notepad File Name\n")
print(47*'\033[1;35;40m-')
np = str(input('\033[1;37;1m[?] Enter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print("\033[1;33;40m", end = "")
print("\033[1;34;40m", end = "")
sp('\33[1m'"\nEnter your name :►\n")
yyy= str(input())
print("\033[1;34;40m", end = "")

print(47*'\033[1;35;40m-')
sp("\033[1m\033[36m[?] Enter The Time Delay In Seconds\n")
print(47*'\033[1;35;40m-')
t = int(input('\033[1;37;1m[?] Enter Time : '))

os.system('clear')
print(logo)

count = 0
while True:
    for line in lines:
        if len(line) > 3:
            if count != 0:
                sleep(t)
            findtextchat(curl)
            sendtextconvo(yyy+ ' ' +line)
            count += 1
            if count % 10 == 0:
                sleep(1)
                clear()
                print("\033[0;37;41m\n")
               
                
