import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=None):
        return self.f.read(n)
    def readall(self):
        return self.f.readall()
    def readinto(self, b):
        return self.f.readinto(b)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)

import unittest

class Test(unittest.TestCase):
    def test(self):
        import io
        self.assertTrue(io.open(__file__) is io.open(File(__file__)))

if __name__ == '__main__':
    unittest.main()
</code>
Which is demonstrating that the same file is returned by <code>io.open</code> when you pass it an object with the file interface or an actual file path.
It should be noted that the file is just wrapped inside an
