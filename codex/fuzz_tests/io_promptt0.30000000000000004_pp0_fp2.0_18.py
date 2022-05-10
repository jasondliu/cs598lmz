import io
# Test io.RawIOBase
class RawIOBase(io.RawIOBase):
    def read(self, n=-1):
        return b"abc"

# Test io.BufferedIOBase
class BufferedIOBase(io.BufferedIOBase):
    def read(self, n=-1):
        return b"abc"

# Test io.TextIOBase
class TextIOBase(io.TextIOBase):
    def read(self, n=-1):
        return b"abc"

# Test io.FileIO
class FileIO(io.FileIO):
    def read(self, n=-1):
        return b"abc"

# Test io.BytesIO
class BytesIO(io.BytesIO):
    def read(self, n=-1):
        return b"abc"

# Test io.StringIO
class StringIO(io.StringIO):
    def read(self, n=-1):
        return b"abc"

# Test io.BufferedReader
class BufferedReader(io.BufferedReader):
    def read(self, n=-1):
        return
