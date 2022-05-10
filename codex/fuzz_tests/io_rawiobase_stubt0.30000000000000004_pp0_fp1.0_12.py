import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.f = open(filename, 'rb')
    def read(self, size=-1):
        return self.f.read(size)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

def read_file(filename):
    return File(filename)

def read_file_as_bytes(filename):
    return open(filename, 'rb').read()

def read_file_as_text(filename):
    return open(filename, 'r').read()

def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def write_file_as_text(filename, data):
    with open(filename, 'w') as f:
        f.write
