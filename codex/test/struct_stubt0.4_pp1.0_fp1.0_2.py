from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

import sys
import struct

def p32(x):
    return struct.pack('<I', x)

def u32(x):
    return struct.unpack('<I', x)[0]

def p64(x):
    return struct.pack('<Q', x)

def u64(x):
    return struct.unpack('<Q', x)[0]

def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def xor_encrypt(data, key):
    cipher = ''
    for i in range(0, len(data), len(key)):
        cipher += xor(data[i:i+len(key)], key)
    return cipher

def encrypt(data, key):
    return xor_encrypt(data, key)

