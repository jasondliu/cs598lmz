import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None
        self.buffer = None
        self.pos = 0
        self.closed = False
        self.open()

    def open(self):
        self.file = open(self.path, self.mode)
        self.buffer = self.file.read()
        self.pos = 0

    def close(self):
        if not self.closed:
            self.closed = True
            self.file.close()

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.buffer) - offset
        else:
            raise ValueError("Invalid whence value")

        return self.pos

    def tell
