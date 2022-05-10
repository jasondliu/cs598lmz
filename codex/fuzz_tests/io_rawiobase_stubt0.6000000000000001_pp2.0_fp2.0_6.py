import io
class File(io.RawIOBase):
    def __init__(self, stream):
        self.stream = stream
    def readinto(self, b):
        return self.stream.readinto(b)
    def read(self, n=-1):
        return self.stream.read(n)
    def write(self, b):
        return self.stream.write(b)
    def seek(self, offset, whence=0):
        return self.stream.seek(offset, whence)
    def tell(self):
        return self.stream.tell()
    def flush(self):
        return self.stream.flush()
    def close(self):
        return self.stream.close()

def open(file, mode='rb'):
    if isinstance(file, str):
        return File(io.open(file, mode=mode))
    return File(file)
