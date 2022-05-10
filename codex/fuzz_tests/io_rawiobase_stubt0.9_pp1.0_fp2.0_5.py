import io
class File(io.RawIOBase):
    def close(self):
        if self.closed:
            return
        try:
            self.flush()
        finally:
            self.closed = True
            if self.closefd:
                self.fd.close()
    @property
    def name(self):
        return self.fd.name
    
f=File()
f.name
f.name
 
 
 
 
f=File()
f.close()
f.close()
f.name
f.name
del f.name
f.name
 
 
 
f.closed
 
 
 
f.name
f.isatty
 
 
 
f.seekable
f.readable
f.writable
class SubFile(File):
    def __init__(self,name):
        self.name=name
f=SubFile("a")
f.name
f.name
f.name='b'
f.name
f.__dict__
 
 
 
class File:
    _name='x'
    @property
    def
