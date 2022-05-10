import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        self.file = open(self.filename, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()

# Example use
with File('/etc/passwd') as f:
    print(f.read())

# Example use
with File('/etc/passwd') as f:
    while True:
        chunk = f.read(8192)
        if not chunk:
            break
        process_chunk(chunk)

# Example use
with File('/etc/passwd') as f:
    b = bytearray(os.path.getsize('/etc/passwd'))

