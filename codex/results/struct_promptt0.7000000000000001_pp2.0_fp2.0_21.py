import _struct
# Test _struct.Struct by instantiating some objects, and
# calling pack, unpack and calcsize.

# Use raw string literals to avoid having to escape backslashes.
struct_codes = r"""biBhHiIlLqQfd"""

def test_struct_b():
    s = _struct.Struct(struct_codes[0])
    vals = (-123, 123, 0)
    for v in vals:
        res = s.pack(v)
        assert len(res) == s.size
        assert s.unpack(res) == (v,)
        assert s.unpack_from(res, 0) == (v,)
        assert s.calcsize(res) == s.size
    # Exercise error conditions.
    raises(struct.error, s.pack)
    raises(struct.error, s.unpack, b"")
    raises(struct.error, s.unpack_from, b"", 0)
    raises(struct.error, s.calcsize, b"")

def test_struct_b_format():
    s = _struct.Struct
