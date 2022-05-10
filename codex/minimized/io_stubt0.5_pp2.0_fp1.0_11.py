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
view[0] = 1
try:
    import _testcapi
except ImportError:
    sys.exit(0)
