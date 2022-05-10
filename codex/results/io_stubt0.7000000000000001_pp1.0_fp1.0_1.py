import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import sys
sys.stdin = File()


import a
a.ch = b'\x00' * 0

# a.ch = b'\x00' * 1000
# a.ch = b'\x00' * 10000
# a.ch = b'\x00' * 100000

# a.ch = b'\x00' * 1000000
# a.ch = b'\x00' * 10000000

# a.ch = b'\x00' * 100000000
