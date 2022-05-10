import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return self._file.read(size)
    def readinto(self, b):
        return self._file.readinto(b)
    def write(self, b):
        return self._file.write(b)
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def truncate(self, size=None):
        return self._file.truncate(size)
    def flush(self):
        return self._file.flush()
    def close(self):
        return self._file.close()


class FileObject(io.RawIOBase):
    pass
