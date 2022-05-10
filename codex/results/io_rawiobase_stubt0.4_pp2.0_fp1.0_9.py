import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def seek(self, n):
        return self.f.seek(n)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()

def test_file():
    f = File(open("test_file.py", "rb"))
    print(f.read(2))
    f.write(b"test")
    f.seek(0)
    print(f.read(2))
    f.close()

# test_file()

# io.RawIOBase
# io.BufferedIOBase
# io.TextIOBase
# io.IOBase

# io.RawIOBase
# io.BufferedIOBase
# io.TextIOBase
# io.IOBase

# io.RawIOBase
# io.Buff
