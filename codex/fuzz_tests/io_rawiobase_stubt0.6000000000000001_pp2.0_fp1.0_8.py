import io
class File(io.RawIOBase):
    """
    A file-like object that reads from and writes to the underlying
    :class:`io.RawIOBase` object.
    """
    def __init__(self, raw):
        self.__raw = raw
        self.__offset = 0
        self.__pos = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__raw.close()

    def close(self):
        self.__raw.close()

    @property
    def closed(self):
        return self.__raw.closed

    def fileno(self):
        return self.__raw.fileno()

    def flush(self):
        return self.__raw.flush()

    def isatty(self):
        return self.__raw.isatty()

    def readable(self):
        return self.__raw.readable()

    def readline(self, size=-1):
        if size < 0:
            size = None

        residue = b''
        buf =
