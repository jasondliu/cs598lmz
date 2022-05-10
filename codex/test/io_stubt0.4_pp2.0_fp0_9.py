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

def callback():
    global view
    view[0] = 1

import atexit
atexit.register(callback)

# This will crash if the atexit callback is not called.
import sys
sys.exit()
