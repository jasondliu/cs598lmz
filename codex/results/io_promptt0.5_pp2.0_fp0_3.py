import io
# Test io.RawIOBase
class RawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"rawio"
    def write(self, b):
        print(b)

# Test io.BufferedIOBase
class BufferedIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b"bufferedio"
    def write(self, b):
        print(b)

# Test io.TextIOBase
class TextIO(io.TextIOBase):
    def read(self, n=-1):
        return "textio"
    def write(self, b):
        print(b)

def test_io_base():
    # Test io.IOBase
    rawio = RawIO()
    assert rawio.readable()
    assert rawio.writable()
    assert rawio.seekable()
    assert not rawio.isatty()
    # Test io.RawIOBase
    assert rawio.read() == b"rawio"
    rawio.write(b"rawio")
   
