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
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

with File('file.bin') as f:
    print(f.read(8))

print(f.closed)

# with File('file.bin') as f:
#     print(f.read(8))
#     raise RuntimeError
#     print(f.read(8))

# f = File('file.bin')
# f.open()
# try:
#     print(f.read(8))
#     raise Runtime
