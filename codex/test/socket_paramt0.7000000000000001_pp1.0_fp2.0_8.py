import socket
socket.if_indextoname(2)

from ctypes import *
from ctypes.wintypes import *

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# check if the current user has admin privileges
if is_admin():
    # code that requires admin privileges to run
    print('user is an admin')
else:
    print('user is not an admin')

import socket

ip = socket.gethostbyname('pypi.python.org')
print(ip)

import socket

socket.gethostbyaddr(ip)

import argparse
import sys
import socket
from datetime import datetime

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

