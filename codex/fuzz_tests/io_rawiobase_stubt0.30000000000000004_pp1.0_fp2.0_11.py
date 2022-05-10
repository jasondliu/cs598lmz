import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, 'rb')
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)

class FileReader(object):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, 'rb')
    def close(self):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)

class FileWriter(object):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, 'wb')
    def close(self):
        self.file.close()
    def write(self, data):

