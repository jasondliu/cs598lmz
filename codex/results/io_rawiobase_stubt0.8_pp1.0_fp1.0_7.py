import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
        self.error = False

    def __iter__(self):
        self.open()
        while True:
            line = self.fd.readline().decode("utf-8").strip()
            if len(line) == 0:
                return
            yield line

    def __exit__(self, *args, **kwargs):
        self.close()

    def _fail_if_error(self):
        if self.error:
            raise IOError("File error")

    def open(self):
        if self.fd is None:
            self.fd = open(self.name)

    def close(self):
        if self.fd is not None:
            self.fd.close()
            self.fd = None
            self.error = False

    def seekable(self):
        self._fail_if_error()
        rv = super().seekable()
        return rv

    def readable(self):
        self._fail_if_error()
