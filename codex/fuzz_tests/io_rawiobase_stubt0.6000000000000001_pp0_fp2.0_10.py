import io
class File(io.RawIOBase):
    def __init__(self,file_path,mode=None,*args,**kwargs):
        self.file_path = file_path
        self.mode = mode
        self.args = args
        self.kwargs = kwargs
        self.file = None
        self.__open()
        self.buffer = None
        self.buffer_size = 1024
        self.buffer_mode = 'r'
        self.buffer_offset = 0
        self.buffer_dirty = False
    def __open(self):
        if self.file is None:
            self.file = open(self.file_path,self.mode,*self.args,**self.kwargs)
        return self.file
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __del__(self):
        self.close()
    def __str__(self):
        return self.file.__str__()
    def __enter__(self):
        return self
    def __exit__
