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

print(view)
</code>
This prints <code>b'\x00'</code> on CPython 3.6.2, but <code>b'\x01'</code> on PyPy 5.8.0 (Python 3.5.3).
I'm not sure if this is a bug in PyPy, or if I'm just misusing the API.

