import mmap
# Test mmap.mmap.flush ?

class Dict:
    def __init__(self, name, mode='c', flags=mmap.MAP_PRIVATE, prot=mmap.PROT_READ|mmap.PROT_WRITE, access=mmap.ACCESS_DEFAULT):
        # TODO: support shared memory
        if mode == 'c':
            fd = os.open(name, os.O_CREAT|os.O_RDWR, 0o600)
        else:
            fd = os.open(name, os.O_RDWR)
        self.m = mmap.mmap(fd, 0, flags, prot, access)
        os.close(fd)
        self.m.seek(0)
        self.m.write(struct.pack('Q', 0))
        self.m.flush()
        self.m.seek(0)

    def _get(self, magic, key):
        self.m.seek(magic)
        off = magic
        while True:
            v = self.m.read(8)
