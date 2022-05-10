import mmap


class MmapDict(dict):
    """
    A dict using a mmap file as storage.

    This class is mostly a wrapper around the builtin dict, with the ability to
    synchronize the keys/values to a file.
    """

    def __init__(self, filename, flag='c', prot=mmap.PROT_READ | mmap.PROT_WRITE, access=mmap.ACCESS_DEFAULT):
        super(MmapDict, self).__init__()
        self.filename = filename
        self.flag = flag
        self.prot = prot
        self.access = access
        self.mode = 'c'
        self.map = None

    def __getitem__(self, key):
        if self.mode == 'c':
            return super(MmapDict, self).__getitem__(key)
        else:
            raise RuntimeError("Can't get an item while in the %s mode." % self.mode)

