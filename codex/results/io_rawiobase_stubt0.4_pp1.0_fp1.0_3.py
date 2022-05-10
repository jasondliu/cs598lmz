import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.fd = None
    def open(self):
        self.fd = open(self.filename, 'rb')
    def close(self):
        self.fd.close()
    def read(self, size=-1):
        return self.fd.read(size)
    def seek(self, offset, whence=0):
        self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()
    def __del__(self):
        self.close()

# Create a new file object
f = File('test.txt')

# Open the file
f.open()

# Read the file
print(f.read())

# Close the file
f.close()

# Open the file
with File('test.txt') as f:
    # Read the file
    print(
