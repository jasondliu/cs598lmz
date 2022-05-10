import mmap

class mmap_file(object):
    def __init__(self, filename, length=0, offset=0, access=mmap.ACCESS_WRITE):
        self.filename = filename
        self.length = length
        self.offset = offset
        self.access = access
        self.fd = os.open(self.filename, os.O_RDWR)
        self.fp = os.fdopen(self.fd, 'r+b', 0)
        self.mmap = mmap.mmap(self.fp.fileno(), self.length, access=self.access, offset=self.offset)

    def __getitem__(self, index):
        return self.mmap[index]

    def __setitem__(self, index, value):
        self.mmap[index] = value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __len__(self):
        return self.mmap.size()

