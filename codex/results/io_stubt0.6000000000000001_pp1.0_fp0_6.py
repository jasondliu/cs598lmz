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

import _tkinter
from _tkinter import TclError
del _tkinter
del TclError

import _locale
from _locale import Error
del _locale
del Error

import _socket
from _socket import error
del _socket
del error

import _ssl
from _ssl import SSLError
del _ssl
del SSLError

import _sha3
from _sha3 import SHA3_224
del _sha3
del SHA3_224

import _blake2
from _blake2 import blake2b
del _blake2
del blake2b

import _bz2
from _bz2 import BZ2Compressor
del _bz2
del BZ2Compressor

import _lzma
from _lzma import LZMAD
