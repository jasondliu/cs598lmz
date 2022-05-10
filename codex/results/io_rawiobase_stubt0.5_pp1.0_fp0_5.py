import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def open(self):
        self.file = open(self.file_name)
    def read(self, size=-1):
        return self.file.read(size)
    def close(self):
        self.file.close()
    def readinto(self, b):
        return self.file.readinto(b)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)

class File_test(test.TestCase):
    def test_read(self):
        f = File("/etc/passwd")
        f.open
