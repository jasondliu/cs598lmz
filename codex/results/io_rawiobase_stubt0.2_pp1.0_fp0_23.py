import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

def test():
    import os
    import sys
    import tempfile
    import unittest

    class FileTests(unittest.TestCase):
        def setUp(self):
            self.f = tempfile.TemporaryFile()
            self.f.write(b"abcdefghijklmnop")
            self.f.seek(0)

        def tearDown(self):
            self.f.close()
            self.f = None

        def test_read(self):
            f
