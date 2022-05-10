import io
class File(io.RawIOBase):
    def read(self):
        return b'foobar'

class BytesIO(io.RawIOBase):
    pass

class TextIOBase(io.TextIOBase):
    pass

class StringIO(io.StringIO):
    pass

class BufferedReader(io.BufferedReader):
    def readline(self):
        return 'abc'

class BufferedWriter(io.BufferedWriter):
    def write(self, s):
        pass

class BufferedRWPair(io.BufferedRWPair):
    def write(self, s):
        pass

class BufferedRandom(io.BufferedRandom):
    def read(self):
        return b'abc'
    def write(self, s):
        pass

class FileIO(io.FileIO):
    pass
