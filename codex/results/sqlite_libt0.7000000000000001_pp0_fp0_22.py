import ctypes
import ctypes.util
import threading
import sqlite3
import socket
import struct
import os
import subprocess

def getmac(interface):
    """
    return mac address of interface
    """
    # Reference:
    # http://code.activestate.com/recipes/439093-get-the-mac-address-of-the-computer/
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', interface[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

def get_cached_mac():
    """
    a simple mac address cache mechanism, cache mac address in /tmp/mac
    """
    if os.path.exists('/tmp/mac'):
        with open('/tmp/mac', 'r') as f:
            return f.read()

    mac = getmac('eth0')
    with open('/tmp/mac', 'w
