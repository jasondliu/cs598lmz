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

view[0] = 0

# Test that the buffer is not referenced anymore

# XXX: This test fails with CPython 3.2 and 3.3, the buffer is still
# referenced.  See issue #20458.

import gc
gc.collect()
del view
gc.collect()

import _testcapi
_testcapi.keepalive_until_here(view)
