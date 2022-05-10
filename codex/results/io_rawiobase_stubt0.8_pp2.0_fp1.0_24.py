import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode = 'r'):
        super(File, self).__init__()
        self.fd = os.open(filepath, os.O_RDONLY)
        self.descriptor = self.fd
        self.mode = mode
        self.closed = False

    def read(self, size):
        return os.read(self.fd, size)

    def close(self):
        if not self.closed:
            os.close(self.fd)
            self.closed = True

def calc_md5(filename):
    m = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
            
def test_unpack(filename):
    with open(filename, 'rb') as f:
        unpack(f, sys.stdout)

def test_unpack_bytes(byte_string):

