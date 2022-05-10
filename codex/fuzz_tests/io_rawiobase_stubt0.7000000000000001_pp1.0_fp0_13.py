import io
class File(io.RawIOBase):
    """A file-like object whose :meth:`~file.read` method simply returns
    an empty byte string.

    This is useful for e.g. :func:`~multiprocessing.Pool`, which refuses to
    pickle file objects.
    """

    def readable(self):
        return True

    def read(self, count=-1):
        return b""


class NullFile(io.RawIOBase):
    """A file-like object whose :meth:`~file.read` method simply returns
    an empty byte string.

    This is useful for e.g. :func:`~multiprocessing.Pool`, which refuses to
    pickle file objects.
    """

    def __init__(self, name=None):
        self._name = name

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def read(self, count=-1):
        return b""

    def write(self, b):
        pass

    def flush
