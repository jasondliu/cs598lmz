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
assert view == b'abc'

# Next test is for non-buffered I/O at least with Python 3:
f = File()
try:
    f.readinto(bytearray(b'abc'))
except AttributeError:
    print("SKIP")
    raise SystemExit
else:
    del f
    import ctypes
    buf = ctypes.create_string_buffer(b'abc')
    del buf
    import gc; gc.collect()
    assert view == b'abc'
