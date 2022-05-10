import io
class File(io.RawIOBase):
    __module__ = _io.__name__
    _io = _io


_StringIO = StringIO

class StringIO(io.StringIO):
    __module__ = _io.__name__
    _io = _io

BytesIO = io.BytesIO

class TextIOWrapper(io.TextIOWrapper, _TextIOBase):
    __module__ = _io.__name__
    _io = _io


class BufferedRandom(io.BufferedRandom, io.RawIOBase):
    __module__ = _io.__name__
    _io = _io
