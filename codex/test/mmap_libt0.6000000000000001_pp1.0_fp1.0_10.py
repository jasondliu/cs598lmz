import mmap

class Mmap:
    """
    Mmap class
    """
    def __init__(self, filename, mode='r', offset=0, length=0):
        self.filename = filename
        self.mode = mode
        self.offset = offset
        self.length = length
        self.file_obj = None
        self.map_obj = None
        if self.mode == 'r':
            self.file_obj = open(self.filename, 'rb')
            self.map_obj = mmap.mmap(self.file_obj.fileno(),
                                     0,
                                     prot=mmap.PROT_READ)
        elif self.mode == 'w':
            self.file_obj = open(self.filename, 'wb')
            self.map_obj = mmap.mmap(self.file_obj.fileno(),
                                     0,
                                     prot=mmap.PROT_WRITE)
        elif self.mode == 'rw':
            self.file_obj = open(self.filename, 'r+b')

