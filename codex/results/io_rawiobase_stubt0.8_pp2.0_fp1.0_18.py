import io
class File(io.RawIOBase):
    """An I/O implementation which wraps a python built-in file object."""

    def __init__(self, fileobj):
        self._fileobj = fileobj

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def readinto(self, b):
        return self._fileobj.readinto(b)

    def read(self, n=-1):
        return self._fileobj.read(n)

    def seek(self, offset, whence=0):
        return self._fileobj.seek(offset, whence)

    def tell(self):
        return self._fileobj.tell()

    def fileno(self):
        return self._fileobj.fileno()

    def truncate(self, pos=None):
        return self._fileobj.truncate(pos)

    def __getstate__(self):
        raise NotImplementedError("File cannot be serialized")


class StringIO(io.BytesIO):
    def __init__(self, value
