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

print(view)

from io import BytesIO
from weakref import proxy

o = object()
b = BytesIO()

# This is the key line, it's the only one that's different from the CPython
# reference leak.
b._snapshot = proxy(o)

del b

print(o)
