import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def close(self):
        return self.f.close()

def test(f):
    f = File(f)
    print(f.read())
    f.write(b"hello")
    f.close()

test(io.BytesIO(b"hello"))
test(io.StringIO("hello"))

# io.TextIOWrapper
# io.BufferedReader
# io.BufferedWriter
# io.BufferedRandom
# io.BufferedRWPair
# io.BufferedDictReader
# io.BufferedDictWriter
# io.TextIOWrapper
# io.StringIO
# io.BytesIO
# io.FileIO
# io.BufferedWriter
# io.BufferedReader
# io.BufferedRWPair
# io.
