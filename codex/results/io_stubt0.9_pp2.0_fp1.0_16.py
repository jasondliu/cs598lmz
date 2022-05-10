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

import weakref
assert view.obj is None

# issue 10001
class WrapperIO(io.RawIOBase):
    def __init__(self, obj):
        self.obj = obj
    def readinto(self, b):
        return self.obj.readinto(b)
    def close(self):
        self.obj = None
    def readable(self):
        return True

import copy
def wrap_file(f):
    return WrapperIO(f)

f = io.BytesIO()
keepalive = [f,]
keepalive += [copy.copy(wrap_file(f)) for i in range(3)]
keepalive += [copy.deepcopy(keepalive[-1])] * 3
del keepalive

del keepalive, f, File, WrapperIO, wrap_file, view
