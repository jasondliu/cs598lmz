import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readinto(self, buf):
        return self.fd.read_into(buf)

f = open("ex.txt", "rb")
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf = bytearray(8)
print(f.readinto(buf))
print(buf)

f.seek(0)
buf
