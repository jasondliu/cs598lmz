import mmap
import os
import sys

def answer(f):
    return int(f[0]) * int(f[-10:])
    
def main():
    f = open(sys.argv[1], 'rb')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    a = ''
    while 1:
        c = s.read_byte()
        if c > 47 and c < 58:
            a += chr(c)
        elif len(a) > 0:
            yield a
            a = ''
        if c == 0:
            break

