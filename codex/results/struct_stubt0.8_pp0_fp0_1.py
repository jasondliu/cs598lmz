from _struct import Struct
s = Struct.__new__(Struct)
s.format = '=QQQQ'
s.size = 32
#s.pack()


class SimpleFile(object):
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'wb') as f:
            f.write(data)

    def read(self, length, offset=0):
        with open(self.filename, 'rb') as f:
            f.seek(offset)
            return f.read(length)

    def __len__(self):
        return os.stat(self.filename).st_size

    def __getitem__(self, key):
        if not isinstance(key, slice):
            raise TypeError('Can only slice file')
        start, stop, step = key.start, key.stop, key.step
        if start is None:
            start = 0
        if stop is None:
            stop = len(self)
        if step is not None:
            raise ValueError("The step of slice can't be a given value")
