import io
class File(io.RawIOBase):

    def __init__(self, filename, mode='rb', closefd=True):
        if mode not in set('rwa'):
            raise ValueError("invalid mode {!r} (only 'rb', 'wb', or 'ab' are allowed)".format(mode))
        if '+' in mode:
            raise ValueError("Cannot use closefd when mode is {}".format(mode))
        self._name = filename
        self.mode = mode
        self.closefd = closefd

        try:
            self.fd = os.open(filename, os.O_BINARY | os._O_RDONLY)
        except OSError:
            self.fd = None
            self._closed = True
        else:
            self._closed = False

    def close(self):
        if not self._closed:
            try:
                if self.fd is not None:
                    os.close(self.fd)
            finally:
                self._closed = True
                self.fd = None

    @property
    def closed(self):
        return self._closed
