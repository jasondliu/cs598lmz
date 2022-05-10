import _struct
# Test _struct.Struct
struct = _struct.Struct('i')
assert struct.size == 4
assert struct.pack(42) == b'*\x00\x00\x00'
assert struct.unpack(b'*\x00\x00\x00') == (42,)

# Test _struct.Struct.from_buffer
class S(object):
    def __init__(self):
        self.buf = bytearray(b'\x12\x34\x56\x78\x9a\xbc\xde\xf0')
        self.offset = 0
    def __getitem__(self, idx):
        return self.buf[idx]
    def __len__(self):
        return len(self.buf)

struct = _struct.Struct('i')
assert struct.size == 4
s = S()
assert struct.from_buffer(s).unpack() == (0x12345678,)
s.offset = 4
assert struct.from_buffer(s).unpack() == (0x9abcdef0,)

# Test _struct.
