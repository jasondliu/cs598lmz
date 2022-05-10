import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.f = open(name, mode)
        self.m = mode
    def close(self):
        self.f.close()
        self.f = None
    def read(self, size=-1):
        if 'r' not in self.m:
            raise io.UnsupportedOperation('read')
        return self.f.read(size)
    def write(self, data):
        if 'w' not in self.m:
            raise io.UnsupportedOperation('write')
        return self.f.write(data)
    def fileno(self):
        return self.f.fileno()
    def __getattr__(self, attr):
        return getattr(self.f, attr)

class FileProxy(File):
    def __init__(self, name, mode, proxy):
        super().__init__(name, mode)
        self.proxy = proxy
    def read(self, size=-1):
        data = super().read(size)
        self.proxy.read
