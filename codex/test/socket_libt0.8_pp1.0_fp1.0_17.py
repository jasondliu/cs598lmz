import socket
import struct
import telnetlib

import sys
import time
import threading

sys.setrecursionlimit(1000000)
BUF_SIZE = 1024

def recvuntil(s, txt):
    data = ""
    while data.find(txt) == -1:
        data += s.recv(1)
    return data

def interact(s):
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

# stage 1: leak stack address
# stage 2: leaking libc address (static)
# stage 3: leaking stack address (by system function)
# stage 4: bypass ASLR: using stack address in system function
# stage 5: calculate shellcode address

#s = socket.create_connection(('52.68.31.117', 8361))
#s = socket.create_connection(('chall2.2019.redpwn.net', 4005))
s = socket.create_connection(('localhost', 8361))
#s = socket.create_connection(('localhost', 9999))


