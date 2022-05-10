import io
class File(io.RawIOBase):
    def __init__(self, f, mode):
        self.f = f
        
        if mode not in ['r', 'w', 'rb', 'wb']:
            raise ValueError("File mode must be one of r, w, rb, or wb")
        self.mode = mode
        
        self.closed = False
        self.name = getattr(f, "name", None)

        if self.mode in ['r', 'rb']:
            self.read = f.read

        if self.mode in ['w', 'wb']:
            self.write = f.write
            
    def readable(self):
        return 'r' in self.mode
    
    def writable(self):
        return 'w' in self.mode
        
    def isatty(self):
        return False
    
    def close(self):
        if not self.closed:
            self.f.close()
            self.closed = True

    def __enter__(self):
        return self
    
    def __exit__(self, type, value,
