import socket
# Test socket.if_indextoname works
socket.if_indextoname(0)

from struct import pack
from binascii import hexlify
from ctypes import sizeof, c_char_p, c_uint, c_void_p, create_string_buffer
from ctypes import BigEndianStructure, Union, c_uint16, c_uint32, c_uint64
from ctypes import POINTER, pointer, addressof
from ctypes import c_char, c_int, c_short, c_ushort, c_longlong
from time import time
from socket import AF_INET6, AF_INET, inet_ntoa
from netifaces import AF_LINK, address_families, ifaddresses, interfaces


class ifaddrmsg(BigEndianStructure):
    _fields_ = [('ifa_family', c_ubyte),
                ('ifa_prefixlen', c_ubyte),
                ('ifa_flags', c_ubyte),
                ('ifa_scope', c_ubyte),
                ('ifa_index', c_uint)]

class if
