import io
# Test io.RawIOBase
class rawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"abcdefg"
# Test io.BufferedIOBase
class bufferIO(io.BufferedIOBase):
    def read(self, n=-1):
        return b"abcdefg"
# Test io.TextIOBase
class textIO(io.TextIOBase):
    def read(self, n=-1):
        return b"abcdefg"
# Test io.BytesIO
class bytesIO(io.BytesIO):
    def read(self, n=-1):
        return b"abcdefg"
# Test io.BufferedReader
class bufferedReader(io.BufferedReader):
    def read(self, n=-1):
        return b"abcdefg"
# Test io.BufferedWriter
class bufferedWriter(io.BufferedWriter):
    def write(self, b):
        return len(b)
# Test io.BufferedRWPair
class bufferedRWPair(io.BufferedRWPair):
    def read(
