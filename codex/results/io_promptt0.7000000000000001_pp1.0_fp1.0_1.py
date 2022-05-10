import io
# Test io.RawIOBase
class RawIOBaseSubclass(io.RawIOBase):
    def read(self, size=-1):
        return b""

# Test io.BufferedIOBase
class BufferedIOBaseSubclass(io.BufferedIOBase):
    def read(self, size=-1):
        return b""

# Test io.TextIOBase
class TextIOBaseSubclass(io.TextIOBase):
    def read(self, size=-1):
        return ""

# Test io.FileIO
class FileIO(io.FileIO):
    pass

# Test io.BytesIO
class BytesIO(io.BytesIO):
    pass

# Test io.StringIO
class StringIO(io.StringIO):
    pass

# Test io.TextIOWrapper
class TextIOWrapper(io.TextIOWrapper):
    pass

# Test io.BufferedReader
class BufferedReader(io.BufferedReader):
    pass

# Test io.BufferedWriter
class BufferedWriter(io.BufferedWriter):
    pass

#
