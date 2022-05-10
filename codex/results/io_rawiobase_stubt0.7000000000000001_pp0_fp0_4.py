import io
class File(io.RawIOBase):
    def __init__(self, name, mode="r", buffering=None):
        self.name = name
        self.mode = mode
        self.closed = False
        self.softspace = 0
        self.mode = mode
        self.name = name
        self.newlines = None
        self.encoding = None
        self._saved_mode = mode
        self.buffer = None
        self.buffering = buffering
        self.line_buffering = False
        self.raw = None
        self.offset = 0
        self.mode = mode
        self.buffer = io.BytesIO()

    def flush(self):
        pass

    def readable(self):
        return "r" in self.mode

    def writable(self):
        return "w" in self.mode

    def seekable(self):
        return True

    def __getattr__(self, item):
        return getattr(self.buffer, item)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_
