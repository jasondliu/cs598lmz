import socket
socket.if_indextoname(0x1)

# Assign an IP address to the interface
import netifaces as ni
ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
ip

# Get the OS name
import platform
platform.system()

# Get the hostname
import socket
socket.gethostname()

# Get the MAC address
import uuid
mac = uuid.getnode()
mac

# Get the current date and time
import datetime
now = datetime.datetime.now()
now

# Get the current year
import datetime
now = datetime.datetime.now()
now.year

# List all the files in a directory
import os
os.listdir(".")

# Check if a file exists
import os.path
os.path.isfile('example.txt')

# Delete a file
import os
os.remove('example.txt')

# Download a file from the internet
import urllib.request
