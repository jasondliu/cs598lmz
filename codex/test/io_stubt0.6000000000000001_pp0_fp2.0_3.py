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

# issue #10
import os
os.set_blocking(0, True)
os.set_blocking(0, False)

# issue #12
import sys
sys.stdout.write('a\n')

# issue #13
import time
time.sleep(1)

# issue #15
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
