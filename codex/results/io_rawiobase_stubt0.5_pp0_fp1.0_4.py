import io
class File(io.RawIOBase):
    def __init__(self, path, mode, *args, **kwargs):
        self.__fh = io.open(path, mode, *args, **kwargs)

    def read(self, n):
        return self.__fh.read(n)

    def write(self, s):
        return self.__fh.write(s)

    def close(self):
        self.__fh.close()

    def seek(self, pos, whence=0):
        self.__fh.seek(pos, whence)

    def tell(self):
        return self.__fh.tell()

    def flush(self):
        self.__fh.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

def open(path, mode, *args, **kwargs):
    return File(path, mode, *args, **kwargs)
</code>

