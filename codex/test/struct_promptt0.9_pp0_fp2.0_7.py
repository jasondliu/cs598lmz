import _struct
# Test _struct.Struct
class TestStruct:

    def test_pack_empty(self):
        self.lenTest(_struct.Struct(''), b'')

    def test_pack_c(self):
        s = _struct.Struct('c')
        self.lenTest(s, b'x')
        self.valueTest(s, b'x')
        self.packTest(s, 'x', 97)
        self.packTest(s, b'!', 33) # bytes are ints
        self.errorTest(s, '345')
        self.errorTest(s, ' ')
        self.errorTest(s, '')
        self.errorTest(s, b'spam')
        self.errorTest(s, b'')
        self.packTest(s, '\xf0', 0xf0) # Try two-byte string
        self.unpackTest(s, b'x', 'x')
        self.unpackTest(s, b'!', b'!')

    def test_pack_b(self):
        s = _struct.Struct('b')
