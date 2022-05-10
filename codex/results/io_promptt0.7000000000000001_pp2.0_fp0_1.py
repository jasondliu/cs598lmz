import io
# Test io.RawIOBase
try:
    io.RawIOBase
except AttributeError:
    pass
else:
    class RawIOBaseTest(unittest.TestCase):
        def test_rawiobase(self):
            f = io.RawIOBase()
            def write(self, b):
                print("write: {!r}".format(b))
            def writelines(self, lines):
                print("writelines: {!r}".format(lines))
            def read(self, n=-1):
                print("read: {!r}".format(n))
            def readall(self):
                print("readall")
            def readinto(self, b):
                print("readinto: {!r}".format(b))
            def readline(self, n=-1):
                print("readline: {!r}".format(n))
            def seek(self, offset, whence=0):
                print("seek: {!r}, {!r}".format(offset, whence))
            def tell(self):
                print("tell")
            def trunc
