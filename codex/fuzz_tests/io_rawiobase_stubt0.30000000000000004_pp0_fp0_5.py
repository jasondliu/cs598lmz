import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = io.open(name, "rb")
        self.size = os.fstat(self.fd.fileno()).st_size
    def read(self, size=-1):
        return self.fd.read(size)
    def seek(self, offset, whence=0):
        return self.fd.seek(offset, whence)
    def tell(self):
        return self.fd.tell()
    def close(self):
        return self.fd.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def get_file(path):
    return File(path)

def get_size(path):
    return os.stat(path).st_size

def get_mtime(path):
    return os.stat(path).st_mtime

def get_atime(path):
    return os.stat(path).st_at
