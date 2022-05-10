import io
# Test io.RawIOBase
class RawIO(io.RawIOBase):
    def read(self, size=-1):
        return b"foo"

# Test io.BufferedIOBase
class BufferedIO(io.BufferedIOBase):
    def read(self, size=-1):
        return b"foo"

# Test io.TextIOBase
class TextIO(io.TextIOBase):
    def read(self, size=-1):
        return "foo"

# Test io.BytesIO
class BytesIO(io.BytesIO):
    pass

# Test io.StringIO
class StringIO(io.StringIO):
    pass

# Test io.FileIO
class FileIO(io.FileIO):
    pass

# Test io.BufferedWriter
class BufferedWriter(io.BufferedWriter):
    pass

# Test io.BufferedReader
class BufferedReader(io.BufferedReader):
    pass

# Test io.BufferedRWPair
class BufferedRWPair(io.BufferedRWPair):
    pass

# Test io.
