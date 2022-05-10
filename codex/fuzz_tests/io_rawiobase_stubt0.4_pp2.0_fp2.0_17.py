import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.file.size() + offset
        else:
            raise ValueError("Invalid value for whence")

    def tell(self):
        return self.offset

    def readable(self):
        return True

    def readinto(self, b):
        data = self.file.read(self.offset, len(b))
        b[:len(data)] = data
        self.offset += len(data)
        return len(data)

    def writable(self):
        return True

    def write(self, b):
        self.file.write(self.offset, b)
        self.offset += len(b)
        return len(b)

class FileSystem:
   
