import io
class File(io.RawIOBase):
    def __init__(self):
        self.file = open("test.txt", "r+")
        self.file_content = self.file.read()
        self.buffer = ""
        self.offset = 0
    def read(self, size = -1):
        if size >= 0 and size < len(self.file_content) - self.offset:
            self.buffer = self.file_content[self.offset:self.offset+size]
        elif size < 0:
            self.buffer = self.file_content[self.offset:]
        else:
            self.buffer = self.file_content[self.offset:]
        if size < 0:
            return self.buffer
        return self.buffer
    def seek(self, offset, whence = 0):
        if whence == 0:
            self.buffer = ""
            self.offset = offset
        elif whence == 1:
            self.buffer = ""
            self.offset += offset
        elif whence == 2:
            self.buffer = ""
            self.offset = len(self.file_content
