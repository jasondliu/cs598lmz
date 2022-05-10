import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import os
os.startfile("file.txt")

import webbrowser
webbrowser.open("https://www.google.com")

import urllib.request
response = urllib.request.urlopen("https://www.google.com")
print(response.read())

import urllib.request
response = urllib.request.urlopen("https://www.google.com")
print(response.read())

import subprocess
subprocess.Popen(["start", "notepad.exe"])

import urllib.request
import subprocess

response = urllib.request.urlopen("https://www.google.com")
print(response.read())

subprocess.Popen(["start", "https://www.google.com"], shell=True)

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
