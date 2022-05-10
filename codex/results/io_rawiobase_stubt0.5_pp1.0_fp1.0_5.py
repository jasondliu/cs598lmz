import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = -1
    def open(self, mode="r"):
        assert self.fd == -1, "File already open"
        self.fd = os.open(self.name, os.O_RDONLY)
    def close(self):
        assert self.fd != -1, "File not open"
        os.close(self.fd)
        self.fd = -1
    def readinto(self, b):
        assert self.fd != -1, "File not open"
        l = os.read(self.fd, len(b))
        b[:l] = l
        return l

f = File("data.txt")
print(f.name)
f.open()
print(f.fd)
f.close()
print(f.fd)

f = File("data.txt")
print(f.name)
f.open()
print(f.fd)
b = bytearray(10)
l = f.readinto
