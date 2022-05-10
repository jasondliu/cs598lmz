import io
class File(io.RawIOBase):
    def __init__(self, path):
        super(File, self).__init__()
        self.path = path
        self.fd = os.open(path, os.O_RDWR | os.O_CREAT)
        self.cur_pos = 0
    
    def tell(self):
        return self.cur_pos
    
    def seek(self, offset):
        if isinstance(offset, int):
            self.cur_pos = os.lseek(self.fd, offset, 0)
        elif isinstance(offset, tuple):
            self.cur_pos = os.lseek(self.fd, offset[0], offset[1])
        return self.cur_pos
    
    def read(self, n=-1):
        if n == -1:
            ret = bytearray()
            while True:
                read_data = os.read(self.fd, 1024 * 1024 * 5)
                if not read_data:
                    break
                ret.extend(read_data)
            self.cur_pos = os.l
