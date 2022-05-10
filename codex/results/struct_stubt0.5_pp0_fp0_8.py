from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = "I"
s.size = 4

class Unpacker(object):
    def __init__(self, file):
        self.file = file
        self.buf = ''
        self.pos = 0

    def read(self, n):
        while len(self.buf) < self.pos + n:
            d = self.file.read(max(n, 4096))
            if not d:
                raise EOFError
            self.buf += d
        result = self.buf[self.pos:self.pos + n]
        self.pos += n
        return result

    def unpack_int(self):
        data = self.read(4)
        return s.unpack(data)[0]

    def unpack_string(self):
        size = self.unpack_int()
        data = self.read(size)
        return data

    def unpack_list(self):
        size = self.unpack_int()
        result = []
        for
