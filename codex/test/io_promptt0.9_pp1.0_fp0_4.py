import io
# Test io.RawIOBase
class RawIOBaseImpl(io.RawIOBase): # Ignore PyUnusedLocal
    def __init__(self, impl):
        self._impl = impl
    
    def readinto(self, buffer):
        return self._impl.readinto(buffer)
    
    def readable(self):
        return self._impl.readable()
    

# Used by test_fileio
def read_all(file, size=-1):
    data = b''
    while size < 0 or len(data) != size:
        block = file.read(min(size, 16))
        if not block:
            return data  # EOF
        data += block
    return data
