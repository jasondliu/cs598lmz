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
assert view is None
gc.collect()
assert view is None

import weakref
view = None
f = io.BufferedReader(File())
r = weakref.ref(f)
assert r() is f
f.read(1)
f = None
gc.collect()
assert view is None
assert r() is None

# Test that the readinto() method gets called on the underlying
# RawIOBase object when the buffer is too small.

class File(io.RawIOBase):
    def readinto(self, buf):
        self.buf = buf
        return len(buf)
    def readable(self):
        return True

f = io.BufferedReader(File(), 1)
b = bytearray(2)
f.readinto(b)
assert f._file.buf is b

# Issue #7761: __del__ method of BufferedReader is called during
# shutdown, when globals are set to None.

class File(io.RawIOBase):
    def close(self):
        global view
        view = b'closed'

