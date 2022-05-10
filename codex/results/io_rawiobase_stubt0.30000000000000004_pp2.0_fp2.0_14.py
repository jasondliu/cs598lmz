import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def read(self, n=-1):
        return self.fd.read(n)
    def write(self, b):
        return self.fd.write(b)
    def close(self):
        return self.fd.close()

class FileWrapper(object):
    def __init__(self, fd):
        self.fd = fd
    def read(self, n=-1):
        return self.fd.read(n)
    def write(self, b):
        return self.fd.write(b)
    def close(self):
        return self.fd.close()

def test_file_wrapper():
    fd = os.open(__file__, os.O_RDONLY, 0777)
    f = File(fd)
    assert f.read(10) == open(__file__).read(10)
    f.close()

def test_file_wrapper_2():
    fd = os.open(__file__,
