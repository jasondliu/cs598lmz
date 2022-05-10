import io
class File(io.RawIOBase):
    """docstring for File"""
    def __init__(self, path, text = ''):
        super(File, self).__init__()
        self.path = path
        self.text = text
        self.f = open(path, 'w+')
        self.f.write(text)
        self.f.seek(0)
        self.is_close = False

    def read(self, n=0):
        if not n:
            n = len(self.text)
        if n > len(self.text):
            n = len(self.text)
        self.last_read = n
        return self.f.read(n)


    def write(self, content):
        self.f.write(content)
        return len(content)
        

    def readable(self):
        return True

        
    def writable(self):
        return True

        
    def seekable(self):
        return True

        
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)


