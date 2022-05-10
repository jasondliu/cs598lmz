import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.real_file = io.open(name, mode=mode)
    def close(self):
        self.real_file.close()
    def fileno(self): return self.real_file.fileno()
    def seekable(self): return self.real_file.seekable()
    def seek(self, *args): return self.real_file.seek(*args)
    def tell(self): return self.real_file.tell()
    
    def readable(self): return mode in ('r', 'w+', 'r+')
    def writable(self): return mode in ('w','w+', 'r+')
    
    def read(self, *args):
        raise NotImplementedError("Not implemented yet!")
    def write(self, *args):
        raise NotImplementedError("Not implemented yet!")
    def flush(self):
        raise NotImplementedError("Not implemented yet!")


import numpy

