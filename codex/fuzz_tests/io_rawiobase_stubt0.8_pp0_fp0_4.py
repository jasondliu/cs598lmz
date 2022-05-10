import io
class File(io.RawIOBase):
    def __init__(self, filename=None, mode=None):
        self.filename = filename
        self.mode = mode
        self.closed = False
        self.info = None
        self.buffer = io.BytesIO()

    def close(self):
        self.buffer.close()
        self.closed = True
        return self.info

    def seekable(self):
        return self.buffer.seekable()

    def readable(self):
        return self.buffer.readable()

    def writable(self):
        return self.buffer.writable()

    def getvalue(self):
        return self.buffer.getvalue()

    def tell(self):
        return self.buffer.tell()

    def seek(self, offset, whence=io.SEEK_SET):
        return self.buffer.seek(offset, whence)

    def read(self, size=-1):
        return self.buffer.read(size)

    def read1(self, size=-1):
        return self.buffer.read1(size)

    def write(self, b):
