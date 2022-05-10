import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.file = open(name, "rb")
    def readinto(self, buf):
        return self.file.readinto(buf)

buf = bytearray(4)
f = File("ex17.py")
while f.readinto(buf) == len(buf):
    print(buf)
</code>

