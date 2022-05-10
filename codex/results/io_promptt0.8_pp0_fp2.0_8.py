import io
# Test io.RawIOBase

class EmptyRawIO(io.RawIOBase):
    def readable(self):
        return True

# Try without specifying the mode
io.RawIOBase(EmptyRawIO())
# Try with text mode
io.RawIOBase(EmptyRawIO(), 't')
# Try with binary mode
io.RawIOBase(EmptyRawIO(), 'b')
# Try with unknown mode
try:
    io.RawIOBase(EmptyRawIO(), 'x')
except ValueError:
    pass
# Try with both text and binary mode
try:
    io.RawIOBase(EmptyRawIO(), 'tb')
except ValueError:
    pass
# Try passing in a dict
try:
    io.RawIOBase(EmptyRawIO, 't')
except TypeError:
    pass

# Test io.BufferedIOBase
class EmptyBufferedIO(io.BufferedIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

# Try without specifying the mode
io.Buff
