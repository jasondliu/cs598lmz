import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def read(self, size=-1):
        return 'a'*size

    def write(self, b):
        return len(b)

    def tell(self):
        return 0

    def seek(self, offset, whence=0):
        return 0

    def close(self):
        pass

    def flush(self):
        pass

    def fileno(self):
        return 0

    @property
    def closed(self):
        return True

def get_file(name, mode):
    return File(name, mode)

class GetFileTest(unittest.TestCase):
    def test_get_file(self):
        f = get_file("file.txt", "r")
        assert f.read(5) == "aaaaa"
        assert f.read() == ""
        assert f.write("test") == 4
        assert f.tell() == 0
        assert f.seek(0, 0) == 0
        f
