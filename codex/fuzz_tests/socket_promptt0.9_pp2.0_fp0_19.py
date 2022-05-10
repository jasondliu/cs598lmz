import socket
# Test socket.if_indextoname()

import sys, getopt
from socket import socket, AF_PACKET, SOCK_RAW
import fcntl
import struct
from socket import SOL_SOCKET, SO_BINDTODEVICE
from ctypes import *

from socket import socket, htons, inet_aton
from ctypes import *
from struct import pack

from ctypes import *
import struct
import inspect
import ctypes

import os
from packet_utils import *

from ipaddress import ip_address

from ctypes import *


class ip_mreqn(Structure):
    pass
class sockaddr_ll(Structure):
    pass
struct_ip_mreqn._fields_ = [
    ('imr_multiaddr', c_ulong),
    ('imr_address', c_ulong),
    ('imr_ifindex', c_int),
]

struct_ip_mreqn.from_param = lambda x:(x,4)

def inet_pton(family,ipstr):
    if family == socket.AF_INET:

