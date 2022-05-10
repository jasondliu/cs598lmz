import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.offset = 0
        
    def read(self, size=-1):
        if size == -1:
            data = self.file.read()
        else:
            data = self.file.read(size)
        self.offset += len(data)
        return data
    
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
            self.file.seek(offset)
        elif whence == 1:
            self.offset += offset
            self.file.seek(self.offset)
        else:
            raise Exception('invalid whence')
    
    def tell(self):
        return self.offset
    
    def close(self):
        self.file.close()

class FileWrapper:
    def __init__(self, path):
        self.file = File(path)
        self.file.seek(0, 2)
        self.size =
