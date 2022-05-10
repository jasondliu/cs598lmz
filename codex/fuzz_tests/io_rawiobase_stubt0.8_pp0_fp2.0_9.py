import io
class File(io.RawIOBase):
    def __init__(self, file_name=None, file_handle=None, mode=None, encoding=None, newline=None, closefd=True):
        self.file_handle = file_handle
        self.name = file_name
        self.mode = file_handle.mode
        self.encoding = encoding
        self.newline = newline
        self.closefd = closefd
        if self.mode in ['r', 'r+', 'rb', 'rb+']:
            self.readable = True
        else:
            self.readable = False
        if self.mode in ['w', 'w+', 'wb', 'wb+']:
            self.writable = True
        else:
            self.writable = False
        self.seekable = True
    def open(self, file_name, mode='r', encoding=None, newline=None):
        self.name = file_name
        self.mode = mode
        self.encoding = encoding
        self.newline = newline
        if self.mode in ['r', 'r+
