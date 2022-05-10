import io
class File(io.RawIOBase):
    
    def __init__(self, filename, mode='rb'):
        self.fp = open(filename, mode)
        
    def read(self, n=-1):
        return self.fp.read(n)
    
    def write(self, b):
        return self.fp.write(b)
    
    def __getattr__(self, name):
        return getattr(self.fp, name)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.close()
    
    def __iter__(self):
        return iter(self.fp)
    
    def __next__(self):
        return next(self.fp)
    
    def close(self):
        return self.fp.close()
f = File('sample.txt')
f.read()

f.close()
f = File('sample.txt')
f.__enter__()

f.__exit__()
f.read()

f.close()
f = File('sample
