import io
class File(io.RawIOBase):
    def __init__(self, filename=None, mode='rb'):
        self.filename = filename
        self.mode = mode
        self.path = None
        self.fd = None
        if 'b' in mode:
            self.binary_mode = True
        else:
            self.binary_mode = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __iter__(self):
        if self.mode in ('r', 'rU'):
            return self
        else:
            raise IOError("File not open for reading")

    def __next__(self):
        self.line = self.readline()
        return self.line

    @property
    def name(self):
        if not self.path:
            if self.filename:
                self.path = self.filename
        return self.path

    def open(self):
        if not self.filename:
            raise IOError("File or buffer required")

