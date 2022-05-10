import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def __enter__(self):
        self.file = open(self.name, 'r')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
with File('/etc/passwd') as f:
    print(f.read())

class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def __enter__(self):
        self.file = open(self.name, 'r')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    def readable(self):
        return True
    def readinto(self, b):
        return self
