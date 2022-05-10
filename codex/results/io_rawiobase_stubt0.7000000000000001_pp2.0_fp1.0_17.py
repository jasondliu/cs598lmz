import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        self.name = getattr(file, 'name',None)
        io.RawIOBase.__init__(self)
    def read(self, n=-1):
        return self._file.read(n)
    def write(self, b):
        return self._file.write(b)
    def close(self):
        return self._file.close()
    def fileno(self):
        return self._file.fileno()
    def tell(self):
        return self._file.tell()
    def seek(self, *args):
        return self._file.seek(*args)
    def flush(self):
        return self._file.flush()
    @property
    def closed(self):
        return self._file.closed
    def __repr__(self):
        return '<File {}>'.format(self._file.name)
    def __getattr__(self, name):
        return getattr(self._file, name)


