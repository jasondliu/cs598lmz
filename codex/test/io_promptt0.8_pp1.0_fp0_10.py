import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self, read_mode):
        self.read_mode = read_mode

    def readinto(self, b):
        return 0

    def readable(self):
        return self.read_mode

# A file that can be used only in binary mode
class BinaryFile(io.FileIO):
    def __init__(self, name, mode):
        io.FileIO.__init__(self, name, mode)
        self._mode = mode

    def write(self, b):
        if 'b' not in self._mode:
            raise ValueError("binary mode required")
        io.FileIO.write(self, b)

# Create a file, write something inside and read it
bin_file = BinaryFile("bin_file", "wb")
