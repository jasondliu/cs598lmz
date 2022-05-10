import io
# Test io.RawIOBase, which is available in Python 3
# but not in Python 2.
class RawIOB(io.RawIOBase):
    def readinto(self, buf):
        return len(buf)

r = RawIOB()
print(r.readinto(b'a'))
# Test io.BufferedIOBase, which is available in Python 3
# but not in Python 2.
class BufferedIOB(io.BufferedIOBase):
    def readinto(self, buf):
        return len(buf)

b = BufferedIOB()
print(b.readinto(b'a'))
# Test io.BytesIO, which is available in Python 3
# but not in Python 2.
bi = io.BytesIO()
print(bi.readinto(b'a'))
# Test io.StringIO, which is available in Python 3
# but not in Python 2.
si = io.StringIO()
print(si.readinto(b'a'))
# Test io.TextIOWrapper, which is available in Python 3
# but not in Python 2.
t
