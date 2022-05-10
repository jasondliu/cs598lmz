import io
class File(io.RawIOBase):
    def __init__(self, file_name, mode, buffering = 0, encoding = None, errors = None, newline = None, closefd = True, opener = None):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        if self.encoding is not None and buffering != 0:
            raise ValueError("encoding or errors without buffering")
        
        if self.encoding is None and self.errors is not None:
            raise ValueError("errors without encoding")
        
        if opener is not None and buffering != 0:
            raise ValueError("opener with buffering")
        
        self.file_object = open(self.file_name, self.mode, self.buffering, self.encoding, self.errors, self.newline, self.closefd, self.opener)
        return
    
    def read(self, size = -1):

