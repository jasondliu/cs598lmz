import io
# Test io.RawIOBase
class RawIOTest(BaseTestIO):
    io_mode = 'r'
    raw_mode = 'r'
    raw_io_mode = 'r'
    def readall(self, f):
        return f.readall()

    def readinto1(self, f, b):
        n = f.readinto(b)
        if n is None:
            n = len(b)
        return n

    def readinto2(self, f, b):
        return f.readinto(b)

    def truncate(self, f, pos=None):
        if pos is None:
            pos = f.tell()
        f.truncate(pos)

    def tell(self, f):
        return f.tell()

    def seek(self, f, pos, whence=io.SEEK_SET):
        f.seek(pos, whence)

    def readable(self, f):
        return f.readable()

    def writable(self, f):
        return f.writable()

    def seekable(self, f):
       
