import _struct
import _binascii

class Parser:
    def __init__(self, b):
        self._data = b

    def read_byte(self):
        return bytes(self._data[:1])

    def consume_byte(self):
        self._data = self._data[1:]

    def read_variable_bytes(self):
        n = self.read_byte()[0]
        return self.read(n)

    def read(self, length):
        return bytes(self._data[:length])

    def consume(self, length):
        self._data = self._data[length:]

    def read_string(self):
        s = self.read_variable_bytes()
        return s.decode('utf-8')

    def read_long_long(self):
        return _struct.unpack("<Q", self.read(8))[0]

    def read_int(self):
        return int.from_bytes(self.read(4), byteorder='little', signed=True)

    def read_fixed_bytes(
