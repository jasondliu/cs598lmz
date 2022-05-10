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

collect()
assert view == b"\x00"

# Issue #8196: segfault when trying to read file object without readable()
buf = bytearray(10)
try:
    n = 0
    while n < len(buf):
        n += f.readinto(buf)
except Exception:
    pass

# Issue #14975: the file objects created by io.StringIO() are supposed to be
# not closed by GC.
try:
    import ctypes
except ImportError:
    pass
else:
    has_close = [False]
    def my_close(*args):
        has_close[0] = True
    ctypes.pythonapi.PyFile_SetCloseFile(id(f), my_close)
    collect()
    assert not has_close[0]
