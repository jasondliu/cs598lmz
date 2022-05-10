import io
# Test io.RawIOBase memoryview.readinto

# StringIO is the obvious example,
# but we would have to build a custom BytesIO subclass
# to test the last method (readinto with a non-empty buffer)

class io_RawIOBase_readinto(object):
    def __init__(self):
        self.data = b"abcde"
        self.pos = 0
        self.closed = False
  
