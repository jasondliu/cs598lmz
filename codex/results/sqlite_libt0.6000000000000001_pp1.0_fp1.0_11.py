import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys
import socket
import struct
import fcntl

# global variables
global_dns_cache = {}
global_dns_cache_lock = threading.Lock()
global_db_conn = None
global_db_conn_lock = threading.Lock()

def get_network_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    finally:
        s.close()

def get_status(host):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((host, 3306))
        status = sock.recv(4096)

