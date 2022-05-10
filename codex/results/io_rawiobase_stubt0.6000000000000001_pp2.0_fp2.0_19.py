import io
class File(io.RawIOBase):
    def __init__(self, path, mode_str):
        self.path = path
        self.mode_str = mode_str
        self.fd = io.open(self.path, self.mode_str)
    def read(self, size=-1):
        return self.fd.read(size)
    def write(self, buf):
        return self.fd.write(buf)
    def close(self, *args, **kwargs):
        return self.fd.close(*args, **kwargs)
    def __enter__(self):
        return self
    def __exit__(self, *args, **kwargs):
        return self.fd.__exit__(*args, **kwargs)
    def tell(self):
        return self.fd.tell()
    def seek(self, offset, whence=io.SEEK_SET):
        return self.fd.seek(offset, whence)
    def __iter__(self):
        return self.fd.__iter__()
    def __next__(self):
        return self.fd.__next__
