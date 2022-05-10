import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None

    def open(self):
        self.fd = os.open(self.path, os.O_RDONLY)
        return self

    def __enter__(self):
        return self.open()

    def __exit__(self, type, value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def readable(self):
        return True

    def readinto(self, buf):
        return os.read(self.fd, buf)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

# Use the new file object with the with statement.
with File('/tmp/data.bin') as f:
    for chunk in iter(lambda: f.read(4), b''):
        print(chunk)
</code>
This code is from the article:
https://realpython.com/python-os-module
