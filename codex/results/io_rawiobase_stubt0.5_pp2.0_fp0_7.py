import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()

def _ensure_binary(f):
    if isinstance(f, str):
        return open(f, 'rb')
    elif isinstance(f, bytes):
        return io.BytesIO(f)
    elif isinstance(f, io.RawIOBase):
        return File(f)
    else:
        raise TypeError('f must be str, bytes or RawIOBase')

def _ensure_text(f):
    if isinstance(f, str):
        return open(f
