import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size = -1):
        if size == -1:
            return open(self.name, 'rb').read()
        else:
            return open(self.name, 'rb').read(size)
    def readinto(self, b):
        b[:] = open(self.name, 'rb').read(len(b))
    def readall(self):
        return open(self.name, 'rb').read()
    def fileno(self):
        return 0
    def write(self, data):
        raise NotImplementedError
    def close(self):
        pass

def main(args):
    try:
        os.mkdir('/tmp/pypy')
    except OSError:
        pass
    os.chdir('/tmp/pypy')
    session = pypy_fuse.Session(args, File)
    session.run()

if __name__ == '__main__':
    main(sys.arg
