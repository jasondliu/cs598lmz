import io
class File(io.RawIOBase):
    def __init__(self,file_path):
        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.file_handler = open(file_path,'rb')
        self.file_handler.seek(0,io.SEEK_SET)
        self.read_size = 0
    def read(self,n):
        if self.read_size + n > self.file_size:
            n = self.file_size - self.read_size
        self.read_size += n
        return self.file_handler.read(n)
    def seek(self,offset,whence):
        if whence == io.SEEK_SET:
            self.file_handler.seek(offset,whence)
            self.read_size = offset
        elif whence == io.SEEK_CUR:
            self.file_handler.seek(offset,whence)
            self.read_size += offset
        elif whence == io.SEEK_END:
            self.file_handler
