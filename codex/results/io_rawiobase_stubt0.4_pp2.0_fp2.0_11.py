import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
        self.opened = False
        self.mode = None
        self.softspace = False

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

    def __str__(self):
        return self.name

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line

    def open(self, mode='r'):
        if self.opened:
            if self.mode != mode:
                raise ValueError('File already opened in different mode')
            return
        self.file = open(self.name, mode)
        self.opened = True
        self.mode = mode
