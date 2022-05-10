import io
class File(io.RawIOBase):
    def __init__(self, fname, mode):
        self.fname = fname
        self.mode = mode
        self.offset = 0

    def readinto(self, b):
        with open(self.fname, self.mode) as file:
            file.seek(self.offset)
            num_bytes = file.readinto(b)
            self.offset += num_bytes
            return num_bytes

    def tell(self):
        return self.offset

f = File('/tmp/foo.txt', 'r')
x = f.readinto(memoryview(bytearray(32)))
print(x)
f.seek(10)
x = f.readinto(memoryview(bytearray(32)))
print(x)
