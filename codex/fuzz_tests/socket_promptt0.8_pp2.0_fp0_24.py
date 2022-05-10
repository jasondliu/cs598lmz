import socket
# Test socket.if_indextoname()
interface = 'eth0'
print(socket.if_indextoname(interface))
print(socket.gethostname())
# Get IP from interface
import socket

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print(get_ip_address('eth0'))

import sys
import os

print(sys.path)

from os.path import expanduser
home = expanduser("~")
print(home)
print(os.getcwd())
# Get CPU and Memory usage
import psutil

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    return psutil.virtual_memory().percent

print(get_cpu
