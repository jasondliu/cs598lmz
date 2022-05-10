import io
class File(io.RawIOBase):

    def __init__(self, file, mode="r"):
        super(File, self).__init__()
        self.file = file
        self.mode = mode
        return

    def read(self, size=-1):
        return self.file.read(size)

    def write(self, b):
        return self.file.write(b)

    def close(self):
        return self.file.close()

    def __next__(self):
        line = self.file.readline()
        if len(line) == 0:
            self.close()
            raise StopIteration
        return line
