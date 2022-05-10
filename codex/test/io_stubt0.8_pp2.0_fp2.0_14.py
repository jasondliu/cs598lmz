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

import ctypes
buf = ctypes.create_string_buffer(b'abc')
del buf
import gc; gc.collect()
