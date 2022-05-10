import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file_name = file_name
        
    def seek(self, offset, whence=0):
        print('File.seek')
        
    def read(self, n=-1):
        print('File.read')
        
        
class Socket(io.RawIOBase):
    def __init__(self, socket):
        self.socket = socket
        
    def seek(self, offset, whence=0):
        print('Socket.seek')
        
    def read(self, n=-1):
        print('Socket.read')
    
    
class InputStream(io.TextIOBase):
    def __init__(self, buffer, encoding, errors=None, newline=None, line_buffering=False, write_through=False):
        self.buffer = buffer
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.line_buffering = line_buffering
        self.write_through = write_through
    
    def readline
