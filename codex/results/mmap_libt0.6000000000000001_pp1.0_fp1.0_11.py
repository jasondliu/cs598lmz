import mmap

class MMap(object):
    """
    A wrapper class for mmap.mmap
    """
    def __init__(self, filename, size, prot=mmap.PROT_READ, flags=mmap.MAP_SHARED, offset=0):
        self.mmap = mmap.mmap(os.open(filename, os.O_RDONLY), size, prot, flags, offset)
        self.size = size

    def __getitem__(self, index):
        return self.mmap[index]

    def __setitem__(self, index, value):
        raise mmap.error("mmap doesn't support writing")

    def __getslice__(self, start, end):
        return self.mmap[start:end]

    def __setslice__(self, start, end, value):
        raise mmap.error("mmap doesn't support writing")

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.mmap.__iter__()

    def __
