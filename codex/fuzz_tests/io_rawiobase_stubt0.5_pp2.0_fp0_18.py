import io
class File(io.RawIOBase):
    def __init__(self, path, mode="r"):
        self.path = path
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        if self.file is None:
            self.file = open(self.path, self.mode)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def __del__(self):
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def readable(self):
        return True

    def writable(self):
        return True

    def read(self, n=-1):
        if self.file is None:
            raise ValueError("I/O operation on closed file.")
        return self.file.read(n)

    def write(self, b):
        if self.file is None:
            raise ValueError("I/O operation on closed file.")
        return
