import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f

    def writable(self):
        return False
    def readable(self):
        return True
    def close(self):
        self.f.close()
    def readinto(self, b):
        return self.f.readinto(b)

class BaseDevice(object):
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, 'rb')
        self.file = File(self.f)
        self.offset = 0
        self.size = os.stat(filename).st_size

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, self.filename)

    def close(self):
        self.f.close()

    def seek(self, offset):
        self.f.seek(offset)
        self.offset = offset

    def read(self, length):
        data = self.f.read(length)
        self.offset += len(
