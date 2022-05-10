from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('L', 'little', '<')

def to_i64(b):
    v, = s.unpack(b)
    if v & 0x8000000000000000:
        v -= 0x10000000000000000
    return v

def to_str(b):
    return b.decode('ascii')

class Item:

    def __init__(self, data):
        self.data = data

    def to_str(self):
        return to_str(self.data)

    def to_ui64(self):
        return int.from_bytes(self.data, 'little', signed=False)

    def to_i64(self):
        return to_i64(self.data)

    def to_f64(self):
        return struct.unpack('<d', self.data)[0]

class Block:

    def __init__(self, f, begin, end, header_size=16, overflow=None):
        self.f = f
        self.begin = begin
        self.end = end

