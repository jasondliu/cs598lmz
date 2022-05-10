import io
# Test io.RawIOBase
# Test io.RawIOBase constructor, close, and fileno()
# Test io.RawIOBase isatty(), not implemented
# Test io.RawIOBase readable(), writable()
# Test io.RawIOBase readall()
# Test io.RawIOBase read(), read() with size
# Test io.RawIOBase read(), read() with size and offset
# Test io.RawIOBase readinto(), readinto() with size
# Test io.RawIOBase readinto(), readinto() with size and offset
# Test io.RawIOBase write(), write() with size
# Test io.RawIOBase write() exception
# Test io.RawIOBase writable(), not implemented

# create a subclass of io.RawIOBase to test, raising
# exceptions from os.read/os.write
class UnsupportedIO(io.RawIOBase):

    def __init__(self):
        self._open = True

    def close(self):
        if not self._open:
            raise ValueError("Unknown I/O operation")
        self._open = False

