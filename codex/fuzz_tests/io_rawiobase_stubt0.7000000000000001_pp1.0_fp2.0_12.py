import io
class File(io.RawIOBase):
    """
    Wrapper around the file object.

    The file is treated as a binary object (i.e., read and write methods use
    byte objects). The seek and tell methods are supported.

    Args:
        fileobj: the file object (an instance of io.IOBase).
    """
    def __init__(self, fileobj):
        super().__init__()
        self._fileobj = fileobj

    def read(self, size=None):
        return self._fileobj.read(size)

    def write(self, b):
        self._fileobj.write(b)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._fileobj.seek(offset, whence)

    def tell(self):
        return self._fileobj.tell()

    def _writable(self):
        return True

    def _readable(self):
        return True

    def close(self):
        self._fileobj.close()

    def flush(self):
        self._fileobj.flush()

    @property
    def closed
