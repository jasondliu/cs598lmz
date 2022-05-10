import io
class File(io.RawIOBase):
    pass

class FileIO(io.FileIO):
    pass


class StringIO(io.StringIO):
    pass

class BytesIO(io.BytesIO):
    pass

class BufferedIOBase(io.RawIOBase):
    pass


class BufferedWriter(io.BufferedWriter):
    pass

class BufferedReader(io.BufferedReader):
    pass

class BufferedRWPair(io.BufferedRWPair):
    pass


class BufferedRandom(io.BufferedRandom):
    
    def lock(self):
        pass

    def unlock(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


class TextIOBase(io.IOBase):
    pass

class TextIOWrapper(TextIOBase):
    pass

class TextIOBase(io.IOBase):
    pass

class IncrementalNewlineDecoder(object):
    pass

class TextIOWrapper(io.TextIOWrapper):

