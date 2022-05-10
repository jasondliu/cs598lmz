import io
class File(io.RawIOBase):  # nocover
    """File implement you can use."""

    def __init__(self, name):
        self.name = name
        self.handle = None
        self.closed = True
        self.encoding = 'utf-8'
        self.mode = 'rb+'

    def open(self):  # nocover
        self.handle = open(self.name, self.mode)
        self.closed = False
        self.encoding = 'utf-8'

    def close(self):  # nocover
        if not self.closed:
            self.handle.close()
            self.closed = True

    def write(self, data):
        if isinstance(data, str):
            raw = data.encode(self.encoding)
        elif isinstance(data, bytes):
            raw = data
        else:
            raise TypeError('File.write need str or bytes')
        if self.closed:
            raise ValueError('File closed.')
        self.handle.write(raw)

    def seek(self, offset, whence=
