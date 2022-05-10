import socket
# Test socket.if_indextoname to make sure it exists
socket.if_indextoname(0)

# Import the server class from the socket module
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_RAW, IPPROTO_ICMP, gethostbyname, gethostname, SOL_SOCKET, SO_BROADCAST, timeout, error, SHUT_RDWR
# Import the threading module
from threading import Thread
# Import the constants from the socket module
from socket import SOL_SOCKET, SO_REUSEADDR
# Import the time module
from time import time, sleep
# Import the sys module
import sys
import signal
# Import the os module
import os
# Import the psutil module
import psutil
# Import the platform module
import platform
# Import the subprocess module
import subprocess
# Import the datetime module
from datetime import datetime
# Import the json module
import json

# Import the python-pushsafer module
import pushsafer

# Define the version of the script
version = "v0.8.2"

# Def
