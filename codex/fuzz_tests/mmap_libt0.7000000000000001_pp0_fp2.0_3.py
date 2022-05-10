import mmap

class MmapOutput:
    def __init__(self, filename, file_size=None):
        self.filename = filename
        if file_size:
            self.file_size = file_size
        else:
            self.file_size = os.stat(self.filename)[6]

    def __enter__(self):
        self.fd = open(self.filename, 'r+b')
        self.f = mmap.mmap(self.fd.fileno(), self.file_size)
        return self

    def __exit__(self, *args):
        self.f.close()
        self.fd.close()

    def __getitem__(self, pos):
        if isinstance(pos, slice):
            return self.f.__getitem__(pos)
        else:
            return self.f.__getitem__(slice(pos, pos+1))

    def __setitem__(self, pos, val):
        if isinstance(pos, slice):
            self.f.__setitem__(pos, val)
       
