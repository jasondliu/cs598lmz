import socket
# Test socket.if_indextoname()

import socket
import sys
import struct

def get_if_index(ifname):
    """Return the ifindex of the named interface"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.if_nametoindex(ifname)

def get_if_name(ifindex):
    """Return the name of the interface with the given ifindex"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.if_indextoname(ifindex)

def get_if_names():
    """Return a list of all the available interface names"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.if_nameindex()

def get_if_addrs(ifname):
    """Return a list of all the IP addresses of the named interface"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.if_
