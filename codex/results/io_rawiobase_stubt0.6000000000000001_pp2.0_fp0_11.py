import io
class File(io.RawIOBase):
    def __init__(self, fname):
        self.f = open(fname, 'rb')
        self.fname = fname
        self.size = os.fstat(self.f.fileno()).st_size
    def read(self, n):
        return self.f.read(n)
    def seek(self, n):
        return self.f.seek(n)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

# The File class is a subclass of io.RawIOBase, so it can be used as an argument to any function that takes
# a raw file object. For example:

f = File('data.bin')
data = f.read()

# However, it can also be used as an argument to any function that takes a file object, because it also
# implements all the methods of io.IOBase. For example:

f = File('data.bin')
data = f.read()

# The File class also implements __enter__ and __exit__
