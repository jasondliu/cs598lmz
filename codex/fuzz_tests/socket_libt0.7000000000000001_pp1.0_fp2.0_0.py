import socket
import struct
import fcntl
import threading
import datetime
import sys
import os

def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[0][20:24])
    return ip


def get_broadcast(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bc = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8919,
        struct.pack('256s', ifname[:15])
    )[0][20:24])
    return bc


def get_mac(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcnt
