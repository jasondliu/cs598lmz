import io
class File(io.RawIOBase):
    pass

class StringIO(io.StringIO):
    pass

class BytesIO(io.BytesIO):
    pass

class BufferedReader(io.BufferedReader):
    pass

class BufferedWriter(io.BufferedWriter):
    pass

class BufferedRWPair(io.BufferedRWPair):
    pass

class BufferedRandom(io.BufferedRandom):
    pass

try:
    import cStringIO
except ImportError:
    pass
else:
    class StringIO(cStringIO.StringIO, io.StringIO):
        pass
