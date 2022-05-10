import io
class File(io.RawIOBase):
    def __init__(self, fpath, mode='rb'):
        self._file = io.FileIO(fpath, mode)
        
    def read(self, size=-1):
        return self._file.read(size)
    
    def write(self, b):
        return self._file.write(b)
    
    def _unsupported(self, *args, **kwargs):
        raise NotImplementedError()
    
    fileno = readable = writable = seekable = _unsupported
    
f = File("ex.txt")
for line in f:
    print(line)

f.close()

# Another way of doing the same thing
class AnotherFile(io.RawIOBase):
    def __init__(self, fpath, mode='rb'):
        self._file = open(fpath, mode)
    
    def read(self, size=-1):
        return self._file.read(size)
    
    def write(self, b):
        return self._file.write(b)
    
    def close
