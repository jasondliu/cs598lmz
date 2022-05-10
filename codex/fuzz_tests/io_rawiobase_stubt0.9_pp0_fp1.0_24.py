import io
class File(io.RawIOBase):
    def close(self):
        return raw_file.close(self)
    
    def fileno(self):
        return raw_file.fileno(self)
    
    def flush(self):
        return raw_file.flush(self)
    
    def isatty(self):
        return raw_file.isatty(self)
    
    def readable(self):
        return raw_file.readable(self)
    
    def readinto(self, b):
        return raw_file.readinto(self, b)
    
    def readline(self, limit = -1):
        if limit < 0:
            raise ValueError("Readline limit must be positive")
        chunks = []
        values = raw_file.readinto(self, bytearray(limit))
        chunks.append(values)
        return bytes.join(b'', chunks)
    
    def readlines(self, hint = None):
        return raw_file.readlines(self, hint)
    
    def seek(self, offset, whence = 0):
        return
