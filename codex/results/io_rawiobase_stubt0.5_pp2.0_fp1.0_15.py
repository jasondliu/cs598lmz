import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.filepath = filepath

    def __enter__(self):
        self.file = open(self.filepath, 'rb')
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def readable(self):
        return True

    def readinto(self, b):
        return self.file.readinto(b)

with File('data.txt') as f:
    print(f.read())

# readinto
with File('data.txt') as f:
    b = bytearray(10)
    f.readinto(b)
    print(b)

# readinto
with File('data.txt') as f:
    b = bytearray(10)
    b[:] = f.readinto(b)
    print(b)

# readinto
with File('data.txt') as f:
    b = bytearray(10)
    b[:5] = f.readinto(b
