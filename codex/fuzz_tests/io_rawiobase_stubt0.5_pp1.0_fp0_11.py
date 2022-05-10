import io
class File(io.RawIOBase):
    def __init__(self, f, mode='r'):
        self.f = f
        self.mode = mode
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()
    @property
    def closed(self):
        return self.f.closed
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def fileno(self):
        return self.f.fileno()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()

def open(file, mode='r'):
    return File(file, mode)

if __name__ == '__main__':
    with open('
