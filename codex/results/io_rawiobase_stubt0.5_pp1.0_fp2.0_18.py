import io
class File(io.RawIOBase):
    pass

class Socket(io.RawIOBase):
    pass

class TextIOWrapper(io.TextIOBase):
    pass

class BufferedReader(io.RawIOBase):
    pass

class BufferedWriter(io.RawIOBase):
    pass

class BufferedRWPair(io.RawIOBase):
    pass

class BufferedRandom(io.RawIOBase):
    pass

class BytesIO(io.RawIOBase):
    pass

class StringIO(io.TextIOBase):
    pass

class TextIOBase(io.TextIOBase):
    pass

class RawIOBase(io.RawIOBase):
    pass

class IOBase(io.IOBase):
    pass

class _IOBase(io.IOBase):
    pass

class _TextIOBase(io.TextIOBase):
    pass

class _RawIOBase(io.RawIOBase):
    pass

class _Appendable(io.IOBase):
    pass

class _Writable(io.RawIOBase
