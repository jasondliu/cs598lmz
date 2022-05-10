import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def read(self, n=-1):
        return b""

RawI.readable()

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def read1(self, n=-1):
        return b""

BufferedI.readable()
# Test io.TextIOBase
class TextI(io.TextIOBase):
    def read(self, n=-1):
        return ""

TextI.readable()
# Test io.RawIOBase
class RawO(io.RawIOBase):
    def write(self, b):
        return 0

RawO.writable()

# Test io.BufferedIOBase
class BufferedO(io.BufferedIOBase):
    def write(self, b):
        return 0

BufferedO.writable()
# Test io.TextIOBase
class TextO(io.TextIOBase):
    def write(self, s):
        return 0

TextO.writable()
# Test io.RawIO
