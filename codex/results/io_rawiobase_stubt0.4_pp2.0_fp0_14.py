import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        self.position = 0

    def read(self, size=-1):
        if size == -1:
            return self.file.read()
        else:
            return self.file.read(size)

    def write(self, data):
        return self.file.write(data)

    def close(self):
        self.file.close()

    def seek(self, offset, whence=0):
        if whence == 0:
            self.position = offset
        elif whence == 1:
            self.position += offset
        elif whence == 2:
            self.position = self.file.seek(0, 2) + offset
        else:
            raise ValueError("Invalid whence value.")

        self.file.seek(self.position)
        return self.position

    def tell(self):
        return self.position

    def fileno(self):
        return self.file.fileno()

