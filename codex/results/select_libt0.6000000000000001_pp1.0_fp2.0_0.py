import select
import socket
import sys
import time
import struct
import ctypes
import ctypes.util

DNS_HEADER_LENGTH = 12
DNS_QUESTION_LENGTH = 4
DNS_RR_LENGTH = 10

class DNSHeader(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_ushort),
        ("flags", ctypes.c_ushort),
        ("qdcount", ctypes.c_ushort),
        ("ancount", ctypes.c_ushort),
        ("nscount", ctypes.c_ushort),
        ("arcount", ctypes.c_ushort)
    ]

    def __new__(self, buffer=None):
        return self.from_buffer_copy(buffer)

    def __init__(self, buffer=None):
        self.id = socket.htons(self.id)
        self.flags = socket.htons(self.flags)
        self.qdcount = socket.htons(self.qdcount)
        self.ancount
