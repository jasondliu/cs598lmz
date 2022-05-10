import io
class File(io.RawIOBase):
    """
    A file like object representing a (possibly remote) file.
    """

    def __init__(self, client, path):
        self._client = client
        self._path = path

    @property
    def name(self):
        return self._path

    @property
    def mode(self):
        return 'rb'

    def close(self):
        pass

    def fileno(self):
        raise NotImplementedError()

    def flush(self):
        pass

    def isatty(self):
        return False

    def readable(self):
        return True

    def readline(self):
        return self._client.read_block(self._path, 0, 1)[0]

    def readlines(self):
        return self._client.read_block(self._path, 0, -1)

    def seek(self, offset, whence=io.SEEK_SET):
        return self._client.seek(self._path, offset, whence)

    def seekable(self):
        return True

    def tell(self):
        return
