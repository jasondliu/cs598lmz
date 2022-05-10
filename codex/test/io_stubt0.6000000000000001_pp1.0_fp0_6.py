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
del File

import _gdbm
d = _gdbm.open('test', 'c')
d.close()
del d
del _gdbm

import _curses
from _curses import error
del _curses
del error

