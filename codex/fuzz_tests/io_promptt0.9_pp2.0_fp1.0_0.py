import io
# Test io.RawIOBase
class BytesRawIO(io.RawIOBase):
    def readline(self):
        pass
    def writelines(self, lines):
        pass
    def readable(self):
        return True
    def writable(self):
        return False
