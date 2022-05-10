import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def readinto(self, b):
        return self.f.readinto(b)

def get_file_as_bytes(f):
    return File(f)

class InMemoryFile(io.BytesIO):
    def __init__(self, f):
        self.f = f
    def readinto(self, b):
        return self.f.readinto(b)

def get_bytes_as_file(b):
    return InMemoryFile(b)
