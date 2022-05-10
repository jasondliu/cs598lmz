import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        super(File, self).__init__()
        self.filename = filename
        self.mode = mode
    def read(self, size=-1):
        print('read({})'.format(size))
    def write(self, b):
        print('write({})'.format(len(b)))
    def seekable(self):
        return False
    def seek(self, offset, whence=0):
        raise io.UnsupportedOperation
    def tell(self):
        raise io.UnsupportedOperation
    def fileno(self):
        raise io.UnsupportedOperation
    def flush(self):
        print('flush')
    def close(self):
        print('close')
f = File('test', 'w')
f.write(b'Hello')
f.read(10)
f.close()
'''
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        super(File, self).__init__()
        self.filename = filename
        self.mode
