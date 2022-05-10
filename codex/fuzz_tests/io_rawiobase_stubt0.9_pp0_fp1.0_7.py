import io
class File(io.RawIOBase):
    """A file-like object exposing the os.FileIO protocol."""
    def __init__(self, path, *args, **kwargs):
        self._file = None
        self._path = path
        self.open(path, *args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __del__(self):
        if self._file:
            try:
                self.close()
            except:
                pass # Emtpy the garbage collector!

    def seek(self, offset, whence=os.SEEK_SET):
        return self._file.seek(offset, whence)

    def tell(self):
        return self._file.tell()

    def open(self, path, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if self._file:
            raise IOError("File is already open")

        self._file = os.open(path, mode)

