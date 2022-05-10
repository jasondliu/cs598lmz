import io
class File(io.RawIOBase):
    pass

class TemporaryFile(File):
    pass

class SpooledTemporaryFile(TemporaryFile):
    pass

class NamedTemporaryFile(File):
    def __init__(self, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None):
        pass

class _TemporaryFileWrapper:
    pass

class _TemporaryDummyFile:
    pass

class TemporaryDirectory:
    # Could be implemented using a context manager
    pass

class IncrementalNewlineDecoder:
    pass

class BufferedReader(File):
    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE):
        pass

class BufferedWriter(File):
    def __init__(self, raw, buffer_size=DEFAULT_BUFFER_SIZE):
        pass

class BufferedRWPair(File):
    def __init__(self, reader, writer, buffer_size=DEFAULT_BUFFER_SIZE):
        pass

class Buff
