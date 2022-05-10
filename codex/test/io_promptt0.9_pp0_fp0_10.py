import io
# Test io.RawIOBase
class C(io.RawIOBase):
    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return False

