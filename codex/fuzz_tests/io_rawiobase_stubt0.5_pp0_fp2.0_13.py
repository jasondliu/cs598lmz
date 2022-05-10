import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
        self.open()

    def open(self):
        self.fd = open(self.path, 'rb')

    def close(self):
        if self.fd:
            self.fd.close()
            self.fd = None

    def readinto(self, buf):
        return self.fd.readinto(buf)

def test_file(path):
    f = File(path)
    print(f.read(8))
    print(f.read(8))
    f.close()

if __name__ == '__main__':
    test_file('/tmp/test.txt')
