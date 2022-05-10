import _struct
# Test _struct.Struct

# Test problem with alignment
class S(object):
    def __init__(self, fmt, *args):
        self.s = _struct.Struct(fmt)
        self.args = args
    def pack(self):
        return self.s.pack(*self.args)
    def unpack(self, str):
        return self.s.unpack(str)
    def size(self):
        return self.s.size

def test(fmt, args):
    s = S(fmt, *args)
    packed = s.pack()
