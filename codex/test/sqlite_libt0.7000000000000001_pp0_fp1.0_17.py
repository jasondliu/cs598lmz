import ctypes
import ctypes.util
import threading
import sqlite3
import time
import socket
import struct
import fcntl
import os

class ArpHeader(ctypes.Structure):
    _fields_ = [
        ("htype", ctypes.c_ushort),
        ("ptype", ctypes.c_ushort),
        ("hlen", ctypes.c_ubyte),
        ("plen", ctypes.c_ubyte),
        ("opcode", ctypes.c_ushort),
        ("sender_mac", ctypes.c_ubyte * 6),
        ("sender_ip", ctypes.c_ubyte * 4),
        ("target_mac", ctypes.c_ubyte * 6),
        ("target_ip", ctypes.c_ubyte * 4)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

