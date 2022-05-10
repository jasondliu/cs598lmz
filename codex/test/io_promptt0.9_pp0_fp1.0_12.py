import io
# Test io.RawIOBase
class SimpleRawIO(io.RawIOBase):
    def __init__(self):
        # Create IO buffer
        self.buffer = bytearray(10)

        # Set inital file position
        self.pos = 0

    def read(self, size=-1):
        # Check if end of buffer
        if size < 0 or size > len(self.buffer):
            # Get all data from buffer
            data = self.buffer

            # Clear the buffer
            self.buffer.clear()

            # Set file position to end
            self.pos = len(data)
        else:
            data = self.buffer[0:size]

            self.buffer = self.buffer[size:]

            self.pos += size

        return data

    def write(self, b):
        self.buffer[self.pos:self.pos+len(b)] = b

        self.pos += len(b)

    def seekable(self):
        return super(SimpleRawIO, self).seekable()

    def readable(self):
        return super(SimpleRawIO, self).readable
