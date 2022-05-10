from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hh'
s.size = 4

def calcsize(fmt):
    return s.size

class Struct(object):
    def __init__(self, fmt, data=None):
        self.format = fmt
        self.size = calcsize(fmt)
        if data:
            self.pack_into(data)

    def pack_into(self, buf, offset=0):
        pass

def pack(fmt, v1, v2):
    out = cStringIO()
    s = Struct(fmt)
    s.pack_into(out, 0, v1, v2)
    return out.getvalue()

