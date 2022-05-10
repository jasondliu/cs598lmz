from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<L'
s.size = struct.calcsize(s.format)

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)

def size():
    return s.size


class String(object):
    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = data.data

    def unpack(self):
        return self.data

    def pack(self):
        return self.data

    def size(self):
        return len(self.data)


class StructWrapper(object):
    def __init__(self, struct, data=None):
        self.struct = struct
        if data is not None:
            self.unpack(data)

    def unpack(self, data):
        for name, type in self.struct:
            if type is None:
                continue
            if isinstance(type, tuple):
                type,
