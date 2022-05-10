import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._file = io.open(name, mode)
        self._file.seek(0, io.SEEK_END)
        self._size = self._file.tell()
        self._file.seek(0)
    def read(self, size=-1):
        return self._file.read(size)
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def close(self):
        self._file.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __len__(self):
        return self._size
    def __iter__(self):
        return self
    def __next__(self):
        return self.read()
    def __getattr__
