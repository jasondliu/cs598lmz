import _struct
# Test _struct.Struct class
class TestStruct:
    def __init__(self):
        self.s = _struct.Struct('I 1s I')
        if self.s.size != 9:
            raise RuntimeError("size should be 9")
        d = self.s.pack(254, b'*', 254)
        if len(d) != self.s.size:
            raise RuntimeError("size mismatch")
        if len(self.s.unpack(d)) != 3:
            raise RuntimeError("wrong number of unpacked values")
        # Test native mode
        self.s = _struct.Struct('I 1s I', False)
        if self.s.size != 8:
            raise RuntimeError("size should be 8")
        f = self.s.unpack(d)
        if len(f) != 3:
            raise RuntimeError("wrong number of unpacked values")
        if f[0] != 254:
            raise RuntimeError("wrong value for first item")
        if f[1] != 42:
            raise RuntimeError("wrong value for second item")
        if f[2
