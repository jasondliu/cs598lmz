import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self.fp = open(filename, mode)
    def close(self):
        self.fp.close()
    def readable(self):
        return self.fp.readable()
    def readinto(self, buf):
        return self.fp.readinto(buf)

# Read a file into a buffer.
with File('sample.txt', 'r') as f:
    buf = bytearray(f.readinto(bytearray(1024)))
    print(buf)


# Write a buffer to a file.
with File('sample.txt', 'w') as f:
    f.write(buf)

# Read a file into a buffer.
with File('sample.txt', 'rb') as f:
    buf = bytearray(f.readinto(bytearray(1024)))
    print(buf)
