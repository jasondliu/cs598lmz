import io
class File(io.RawIOBase):
    def __init__(self,filepath):
        self.filepath = filepath
    def read(self,size=-1):
        with open(self.filepath,'rb') as file:
            return file.read(size)
    def write(self,b):
        with open(self.filepath,'wb') as file:
            file.write(b)
    def seek(self,offset,whence=io.SEEK_SET):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return -1
    def isatty(self):
        return False

class FileSystem(object):
    def __init__(self):
        self.filesystem = dict()
    def get_file(self,filepath):
        if filepath not in self.filesystem:
            self.filesystem[filepath] = File(file
