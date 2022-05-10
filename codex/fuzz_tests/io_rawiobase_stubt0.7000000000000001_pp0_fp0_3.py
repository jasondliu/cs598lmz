import io
class File(io.RawIOBase):
    EOF=False
    def __init__(self,fname,mode):
        self.fname=fname
        self.mode=mode
        self.encoding=None
        self.newlines=None
        self.closefd=True
        self.pos=0
        if not os.path.exists(fname):
            with open(fname,'w') as f:
                f.write('')
        self.file=open(self.fname,self.mode)
    def _set_mode(self,mode):
        if mode is None:
            return self.mode
        else:
            return mode
    def _set_encoding(self,encoding):
        if encoding is None:
            return self.encoding
        else:
            return encoding
    def seekable(self):
        if self.file is None:
            raise ValueError('I/O operation on closed file.')
        else:
            return True
    def readable(self):
        if self.file is None:
            raise ValueError('I/O operation on closed
