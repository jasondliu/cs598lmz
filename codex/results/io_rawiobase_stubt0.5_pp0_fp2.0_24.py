import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return '\0' * n
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def flush(self):
        pass
    def fileno(self):
        return 0
    def isatty(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __iter__(self):
        return iter(())
    def __next__(self):
        raise StopIteration
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    @property
    def name(self):
        return ''
    @property
    def mode(self):
        return ''
    @property
    def closed(self):
        return False
    def __repr
