import io
# Test io.RawIOBase.readinto() method

class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.read_return_val = None
        self.read_returns = []
        self.readinto_return_val = None
        self.readinto_returns = []
        self.write_return_val = None
        self.write_returns = []
        self.seek_return_val = None
        self.seek_returns = []
        self.tell_return_val = None
        self.tell_returns = []
        self.truncate_return_val = None
        self.truncate_returns = []
        self.mode = io.DEFAULT_BUFFER_SIZE
        self.buffer = bytearray(self.mode)
        self.pos = 0
        self.closed = False
        self.isatty_return_val = False
        self.flush_returns = []

    def readable(self):
        return True

    def seekable(self):
        return True

