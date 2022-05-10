import io
# Test io.RawIOBase
class RIO(io.RawIOBase):
    def writable(self):
        return False

# Verify preferred exception for write()
