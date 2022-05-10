import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
    def raw_read(self, size):
        try:
            f = open(self.filename, "r+b")
            contents = f.read(size)
            f.close()
            return contents
        except FileNotFoundError:
            return None
    def raw_write(self, data):
        try:
            f = open(self.filename, "ab+")
            f.write(data)
            f.close()
            return len(data)
        except FileNotFoundError:
            return 0

class FileSystem(Readable, Writable):
    def __init__(self, dir = "."):
        self.dir = dir
    def open_file(self, filename):
        return File(self.dir+"/"+filename)

class Driver():
    def __init__(self):
        self.file_system = None
        self.file = None
    def read(self, address, size):
        if self.file_system:
            if self.file
