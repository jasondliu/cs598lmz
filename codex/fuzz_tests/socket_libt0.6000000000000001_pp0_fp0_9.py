import socket
import threading
import time
import os
import sys
import subprocess
import telnetlib
import struct

#
#
#
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

#
#
#
def get_free_port(ip="127.0.0.1", port_range=(8000, 9000)):
    for port in range(port_range[0], port_range[1]):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((ip, port))
            sock.close()
            return port
        except socket.error:
            continue
    return None

#
#
#
def get_free_ports(ip="127.0.0.1", num=1, port_range=(8000, 9000)):
    ports = []
    for port in range(port_range[0],
