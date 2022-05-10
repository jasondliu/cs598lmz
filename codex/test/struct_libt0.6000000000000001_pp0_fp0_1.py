import _struct

class PyBuffer(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def read_int(self):
        self.offset += 4
        return _struct.unpack_from('<I', self.data, self.offset - 4)[0]

    def read_short(self):
        self.offset += 2
        return _struct.unpack_from('<H', self.data, self.offset - 2)[0]

    def read_byte(self):
        self.offset += 1
        return _struct.unpack_from('<B', self.data, self.offset - 1)[0]

    def read_buf(self, length):
        self.offset += length
        return self.data[self.offset - length:self.offset]

    def read_string(self):
        length = self.read_int()
        return self.read_buf(length)

    def read_byte_array(self):
        length = self.read_int()
