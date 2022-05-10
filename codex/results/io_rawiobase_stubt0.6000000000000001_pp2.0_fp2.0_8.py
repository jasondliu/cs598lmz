import io
class File(io.RawIOBase):
    def __init__(self, filepath):
        self.file = open(filepath, 'rb')
        self.read = self.file.read
        self.tell = self.file.tell
        self.seek = self.file.seek
        self.close = self.file.close
    def fileno(self):
        return self.file.fileno()
    def isatty(self):
        return self.file.isatty()
    def readable(self):
        return self.file.readable()
    def seekable(self):
        return self.file.seekable()
    def writable(self):
        return self.file.writable()
    def readinto(self, buffer):
        return self.file.readinto(buffer)

class FileReader(object):
    def __init__(self, file):
        self.file = file
    def read(self):
        return self.file.read()

class FileWriter(object):
    def __init__(self, file):
        self.file = file
    def write(self
