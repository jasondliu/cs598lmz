import socket
import threading
import time
import os
import sys
import random
import string
import platform
import subprocess
import re
import urllib
import urllib2

# Global variables
version = "1.0"

# Check if root
if os.geteuid() != 0:
    sys.exit("[!] Please run this script as root")

# Check internet connection
def check_connection():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

# Get local IP
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = (s.getsockname()[0])
    s.close()
    return ip

# Get local MAC
def get_mac():
    mac = open('/sys/class/net/eth0/address').readline()

