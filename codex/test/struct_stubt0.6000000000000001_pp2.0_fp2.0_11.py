from _struct import Struct
s = Struct.__new__(Struct)
s.format = '=I'
s.size = 4

def p32(n):
    return s.pack(n)

def u32(n):
    return s.unpack(n)[0]

def p64(n):
    return struct.pack('<Q', n)

def u64(n):
    return struct.unpack('<Q', n)[0]

#
#
#

import time

def _recvuntil(s, suffix):
    n = len(suffix)
    buf = ''
    while True:
        c = s.recv(n)
        if not c:
            raise EOFError('recvuntil(%r) failed' % suffix)
        buf += c
        if buf.endswith(suffix):
            return buf

def recvuntil(s, suffix):
    buf = _recvuntil(s, suffix)
