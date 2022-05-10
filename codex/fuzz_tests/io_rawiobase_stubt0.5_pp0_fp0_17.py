import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return False
    def fileno(self):
        return self.f.fileno()
    def close(self):
        return self.f.close()

class FileWrapper(object):
    def __init__(self, f):
        self.f = f
    def write(self, b):
        self.f.write(b)
    def close(self):
        self.f.close()

def wrap_file(f):
    if isinstance(f, io.RawIOBase):
        return File(f)
    else:
        return FileWrapper(f)

def str_to_bytes(s):
    if isinstance(s, str):
        return
