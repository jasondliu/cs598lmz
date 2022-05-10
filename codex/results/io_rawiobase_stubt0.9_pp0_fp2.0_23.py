import io
class File(io.RawIOBase):
    "File(path, *args) -> RawIOBase object\n\nOpen file and return a corresponding file object.\n\'path\' is an string or bytes object"
    def __init__(self, path, *args, **kwargs):
        super(File, self).__init__()
        self.handle = open(path, *args)


class TextFile(io.TextIOBase):
    "TextFile(path, *args) -> TextIOBase object\n\nOpen file and return a corresponding file object.\n\'path\' is an string or bytes object"
    def __init__(self, path, *args, **kwargs):
        super(TextFile, self).__init__()
        self.handle = codecs.open(path, *args)


class Buffer(io.IOBase):
    "Buffer(n) -> IoBase object\n\nReturn an buffered raw IOBase object"
    def __init__(self, size=io.DEFAULT_BUFFER_SIZE):
        super(Buffer, self).__init__()
        self.handle
