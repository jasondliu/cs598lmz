import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.fd = file(path, 'rb')
        self.path = path
        self.buffer = None
        self.buffer_ref = (None, None)
        self.pos = 0
    def close(self):
        self.fd.close()
        del self.fd
        del self.path
        del self.buffer
        del self.buffer_ref
        del self.pos
        return 0
    def fileno(self):
        # FIXME: Use a different method to implement
        # RawIOBase and return a real file descriptor
        return NotImplemented
    def flush(self):
        self.fd.flush()
        return 0
    def isatty(self):
        return False
    def readable(self):
        return True
    def readinto(self, b):
        # FIXME: Consider optimising for large reads
        if not isinstance(b, memoryview):
            b = memoryview(b)
        read = 0
        while read < len(b):
            c = self._read(
