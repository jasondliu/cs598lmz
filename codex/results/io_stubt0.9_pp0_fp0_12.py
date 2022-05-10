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

assert view == b'a'

# Issue 17438
class X:
    def readinto(self, buff):
        global view
        global pos
        view = memoryview(buff)
        pos = buff
class C:
    def __enter__(self):
        return X()
    def __exit__(self, *excinfo):
        pass

with (C()) as v:
    u = memoryview(C())
assert view is u
# this is actually a CPython bug: http://bugs.python.org/issue22318
#assert type(view[0]) is bytearray
assert type(pos[0]) is bytearray
