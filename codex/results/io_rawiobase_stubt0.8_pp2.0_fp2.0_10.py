import io
class File(io.RawIOBase):
    def readall(self):
        self.read()
    def read(self):
        super().read()


class BinaryFile(io.RawIOBase):
    def readall(self):
        self.read()
    def read(self):
        super().read()
