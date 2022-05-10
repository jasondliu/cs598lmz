import _struct
from ctypes import *
import os
import sys
import time
import threading
import struct
from struct import *
import socket
import select
import binascii
from binascii import hexlify
import telnetlib
import re

# Defines
#
#

# Globals
#
#

# Functions
#
#

def send_command(conn, cmd):
    resp = conn.recv(1024)
    print(resp)
    conn.send(cmd)
    print("[+] Sent {}\n".format(cmd))

def parse_data(data):
    printable = set(string.printable)
    data = ''.join(filter(lambda x: x in printable, data))
    data = data.replace('\n', '')
    data = data.replace('\r', '')
    return data

def write_data(conn, data):
    for d in data:
        conn.send(d)
        time.sleep(0.01)

