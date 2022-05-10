import _struct

class BinaryReader:

    def __init__(self, file):
        self.file = file

    def read_int(self):
        return int.from_bytes(self.file.read(4), "little")

    def read_long(self):
        return int.from_bytes(self.file.read(8), "little")

    def read_byte(self):
        return int.from_bytes(self.file.read(1), "little")

    def read_string(self):
        size = self.read_int()
        string = self.file.read(size)
        return string.decode('utf-8')

    def read_bytes(self, size):
        return self.file.read(size)

    def read_short(self):
        return int.from_bytes(self.file.read(2), "little")

    def read_struct(self, fmt):
        size = _struct.calcsize(fmt)
        return _struct.unpack(fmt, self.file.read(size))

