import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = open(name, 'rb')
    def read(self, size=-1):
        return self.file.read(size)
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
    def close(self):
        self.file.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.name)

def get_data(name):
    with File(name) as f:
        return f.read()
