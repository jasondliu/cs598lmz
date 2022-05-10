import io
class File(io.RawIOBase):
    pass

class Socket(io.RawIOBase):
    pass

class StringIO(io.RawIOBase):
    pass

class BytesIO(io.RawIOBase):
    pass

class BufferedIOBase(io.RawIOBase):
    pass

class BufferedReader(BufferedIOBase):
    pass

class BufferedWriter(BufferedIOBase):
    pass

class BufferedRWPair(BufferedReader, BufferedWriter):
    pass

class BufferedRandom(BufferedReader, BufferedWriter):
    pass

class TextIOBase(io.RawIOBase):
    pass

class TextIOWrapper(TextIOBase):
    pass

class StringIO(TextIOBase):
    pass

class IncrementalNewlineDecoder(TextIOBase):
    pass

class FileIO(RawIOBase):
    pass

class BytesIO(RawIOBase):
    pass

class BufferedIOBase(RawIOBase):
    pass

class BufferedReader(BufferedIOBase):
    pass

class Buff
