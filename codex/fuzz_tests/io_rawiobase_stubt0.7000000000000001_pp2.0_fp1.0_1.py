import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b""
    def write(self, b):
        return len(b)
    def seek(self, offset, whence=0):
        pass
    def seekable(self):
        return True
    def tell(self):
        return 0
    def readable(self):
        return True
    def writable(self):
        return True
    def readinto(self, buffer):
        read = self.read()
        size = len(buffer)
        buffer[:len(read)] = read
        return size
    def close(self):
        pass
    def flush(self):
        pass
    def fileno(self):
        return -1

class TextIOWrapper(io.TextIOBase):
    def __init__(self, file, encoding, errors, newline):
        self.file = file
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
    def seek(self, offset, whence=0):
        self.file.seek(offset, whence
