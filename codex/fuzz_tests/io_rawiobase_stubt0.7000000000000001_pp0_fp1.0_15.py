import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return self.buffer.read(n)
 
    def seek(self, offset, whence=0):
        super(File, self).seek(offset, whence)
 
    def write(self, b):
        return super(File, self).write(b)
 
    def tell(self):
        return super(File, self).tell()
 
    def flush(self):
        super(File, self).flush()
 
    def fileno(self):
        return super(File, self).fileno()
 
    def seekable(self):
        return super(File, self).seekable()
 
    def readable(self):
        return super(File, self).readable()
 
    def writable(self):
        return super(File, self).writable()
 
    def __init__(self, buffer, mode='rb'):
        self.buffer = buffer
        self.mode = mode
        io.RawIOBase.__init__(self)
class BlockBlobService(object):

