import socket
import sys
import datetime
import requests
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

is_send = False

def send():
    global is_send
    is_send = True

def get_ip(url):
    try:
        r = requests.get(url)
        text = r.text
        if text:
            return text.strip()
    except:
        pass

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def ip_loop():
    root = tk.Tk()
    root.geometry('300x50')
    root.title('IP Address')
    myfont = tkFont.Font(family='Helvetica', size=20, weight='bold')
   
