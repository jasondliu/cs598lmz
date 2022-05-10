import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.file = open(name, mode)
        return self.file.__init__(name, mode)
