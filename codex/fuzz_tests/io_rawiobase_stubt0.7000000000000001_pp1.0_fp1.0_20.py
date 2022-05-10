import io
class File(io.RawIOBase):
    def __init__(self, file_object):
        self.file_object = file_object
    def readinto(self, b):
        n = len(b) // self.blocksize
        b[:n * self.blocksize] = self.file_object.read(n * self.blocksize)
        return n * self.blocksize
    @property
    def name(self):
        return self.file_object.name
    @property
    def closed(self):
        return self.file_object.closed
    def close(self):
        return self.file_object.close()
    @property
    def mode(self):
        return self.file_object.mode
    def fileno(self):
        return self.file_object.fileno()
class Disk(File):
    blocksize = 512
    def readinto(self, b):
        n = len(b) // self.blocksize
        b[:n * self.blocksize] = self.file_object.read(n * self.blocksize)
        return n * self.blocks
