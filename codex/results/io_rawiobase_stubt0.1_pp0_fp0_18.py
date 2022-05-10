import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()

def test(f):
    f.write(b"hello")
    f.seek(0)
    print(f.read())

test(File(open("test.txt", "wb+")))

# io.TextIOBase
# io.StringIO
# io.BytesIO

# io.BufferedIOBase
# io.BufferedReader
# io.BufferedWriter
# io.BufferedRWPair
# io.BufferedRandom

# io.RawIOBase
# io.FileIO
# io.BytesIO

# io.TextIOBase
# io.StringIO
# io.TextIOWrapper

# io.FileIO
# io.BufferedReader
# io.BufferedWriter
# io.BufferedR
