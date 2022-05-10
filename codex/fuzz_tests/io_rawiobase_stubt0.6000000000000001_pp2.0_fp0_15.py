import io
class File(io.RawIOBase):
    def __init__(self, file_name: str, mode: str = 'rb'):
        self.file_name = file_name
        self.mode = mode
        self.file = None
        self.pos = 0
        self.closed = False
        self.open()

    def open(self, file_name: str = None, mode: str = None):
        if file_name is not None:
            self.file_name = file_name
        if mode is not None:
            self.mode = mode
        self.file = open(self.file_name, self.mode)
        self.closed = False

    def close(self):
        if not self.closed:
            self.file.close()
            self.closed = True

    def fileno(self):
        return self.file.fileno()

    def flush(self):
        return self.file.flush()

    def isatty(self):
        return self.file.isatty()

    def readable(self):
        return self.file.readable()

    def readline(
