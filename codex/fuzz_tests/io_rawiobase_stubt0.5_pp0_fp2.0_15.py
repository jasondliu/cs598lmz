import io
class File(io.RawIOBase):
    def __init__(self):
        self.file = None
        self.file_name = "test.txt"
    def write(self, b):
        print("File write")
        self.file = open(self.file_name, "wb")
        self.file.write(b)
        self.file.close()
    def read(self, size=-1):
        print("File read")
        if self.file == None:
            self.file = open(self.file_name, "rb")
        b = self.file.read(size)
        self.file.close()
        self.file = None
        return b
    def close(self):
        print("File close")
        if self.file != None:
            self.file.close()
            self.file = None

class Buffer(io.RawIOBase):
    def __init__(self):
        self.buffer = []
    def write(self, b):
        print("Buffer write")
        self.buffer.append(b)
    def read(self, size=-1
