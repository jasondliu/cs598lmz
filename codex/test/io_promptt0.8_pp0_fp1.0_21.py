import io
# Test io.RawIOBase.readable() method

class RawIOBase_readable(io.RawIOBase):
    def readable(self):
        return False         # Cannot read

