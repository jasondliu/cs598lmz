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

import gc
gc.collect()

#----------------------
from ctypes import CDLL, CDLL_EXPORT, cast, POINTER, c_char_p, c_void_p, c_int

libc = CDLL("libc.so.6")

libc.malloc.argtypes = [c_int]
libc.malloc.restype = c_void_p
libc.free.argtypes = [c_void_p]

def c_str(s):
    c = cast(libc.malloc(len(s)+1), c_char_p)
    c.value = s
    return c

libc.puts.argtypes = [c_char_p]
libc.puts.restype = c_int

libc.puts(c_str(b"hi from c\n"))
libc.free(c_str(b"hi from c\n"))
#----------------------

#----------------------
from ctypes import *

c = CDLL(None)
c.puts.arg
