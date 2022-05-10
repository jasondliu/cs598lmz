import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.file = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def __repr__(self):
        return "File({!r}, {!r})".format(self.name, self.mode)

    def open(self):
        self.file = open(self.name, self.mode)
        return self

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

    def readable(self):
        return self.mode in ('r', 'r+', 'a+')

    def writable(self):
        return self.mode in ('w', 'w+', 'r+', 'a+')

   
