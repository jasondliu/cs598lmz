import io
# Test io.RawIOBase
class MockRawIO(io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        return len(b)

    def seek(self, offset, whence=0):
        return 0

# Test io.BufferedIOBase
class MockBufferedIO(io.BufferedIOBase):
    def __init__(self):
        self.buffer = bytearray()

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        self.buffer.extend(b)
        return len(b)

    def seek(self, offset, whence=0):
        return 0

    def close(self):
        pass

# Test io.IOBase
class MockIO(io
