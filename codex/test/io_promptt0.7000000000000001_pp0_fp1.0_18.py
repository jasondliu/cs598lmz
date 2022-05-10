import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, write_data):
        self.write_data = write_data
    def readall(self):
        return b''
    def readinto(self, buf):
        if len(self.write_data) == 0:
            return None
        buf[:len(self.write_data)] = self.write_data
        self.write_data = b''
        return len(buf)
    def write(self, b):
        self.write_data += b
        return len(b)
    def readable(self):
        return True
    def seekable(self):
        return False
    def writable(self):
        return True

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw_io):
        self.raw_io = raw_io
        self.read_buffer = b''
    def readall(self):
        read_buffer = self.read_buffer
        self.read
