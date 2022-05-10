import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.fd = None
    def readinto(self, buf):
        if self.fd is None:
            self.fd = open(self.filename, 'rb')
            return self.fd.readinto(buf)
        return 0
    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
f = File('/etc/passwd')
buf = bytearray(8)
f.readinto(buf)
print(buf)
f.close()

buf = bytearray(8)
with File('/etc/passwd') as f:
    f.readinto(buf)
    print(buf)

# 17.1.2.2. BytesIO Objects
data = b'Hello World'
f = io.BytesIO(data)
print(f.read())
f.write(b'This is a test')
print(f.getvalue())

# 17.1.2.3.
