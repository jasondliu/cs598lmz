import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None

    def open(self):
        self.file = open(self.name, 'rb')

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def readinto(self, b):
        return self.file.readinto(b)

f = File('test.txt')
f.open()
b = bytearray(10)
n = f.readinto(b)
print(n)
print(b)
f.close()

# io.BufferedIOBase
# io.BufferedReader
# io.BufferedWriter
# io.BufferedRWPair
# io.BufferedRandom

# io.TextIOBase
# io.TextIOWrapper
# io.StringIO
# io.BytesIO

# io.RawIOBase
# io.FileIO
# io.BytesIO

# io.FileIO
# io.BytesIO
# io.
