import io
class File(io.RawIOBase):
    def __init__(self, path, mode="rb"):
        self.path = path
        self.mode = mode
        self.pos = 0
        if "r" in mode:
            self.fd = open(path, mode)
        else:
            self.fd = None
    
    def read(self, count=-1):
        if self.fd is None:
            print("a")
            self.fd = open(self.path, self.mode)
        res = self.fd.read(count)
        self.pos += len(res)
        return res
    
    def write(self, b):
        if self.fd is None:
            self.fd = open(self.path, self.mode)
        res = self.fd.write(b)
        self.pos += res
        return res
    
    def seek(self, pos, whence=None):
        if whence is None:
            self.pos = pos
        elif whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos +=
