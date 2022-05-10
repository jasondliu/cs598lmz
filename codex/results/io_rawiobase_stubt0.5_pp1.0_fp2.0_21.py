import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b''
    def readinto(self, b):
        return 0
    def write(self, b):
        return len(b)

class FileIO(io.RawIOBase):
    def read(self, n=-1):
        return b''
    def readinto(self, b):
        return 0
    def write(self, b):
        return len(b)

try:
    import _io
    class BufferedReader(_io.BufferedIOBase):
        def read(self, n=-1):
            return b''
        def readinto(self, b):
            return 0
        def write(self, b):
            return len(b)
    class BufferedWriter(_io.BufferedIOBase):
        def read(self, n=-1):
            return b''
        def readinto(self, b):
            return 0
        def write(self, b):
            return len(b)
    class BufferedRWPair(_io.BufferedIOBase):
        def read(self,
