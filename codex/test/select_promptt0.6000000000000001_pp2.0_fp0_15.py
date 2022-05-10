import select
# Test select.select() to see if it's better than time.sleep()
# It isn't...

import time
import struct
import sys
import socket
import telnetlib
import random
import string

from hexdump import hexdump

# This is the same as u32() in pwntools
def p32(x):
	return struct.pack('<I', x)

def u32(x):
	return struct.unpack('<I', x)[0]

def p64(x):
	return struct.pack('<Q', x)

def u64(x):
	return struct.unpack('<Q', x)[0]

def xor(a, b):
	return ''.join([chr(ord(x) ^ ord(y)) for x, y in zip(a, b)])

def readuntil(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

def readline(f):
	return readuntil(f)
