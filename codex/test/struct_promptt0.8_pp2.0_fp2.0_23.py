import _struct
# Test _struct.Struct with a format that has no type modifiers,
# and tries various alignment options.
Struct = _struct.Struct
unpack = Struct.unpack

def doformat(fmt):
    fmt = fmt + "S"
    s = Struct(fmt)
    data = s.pack(1, 2, 3.0, 4.0, 5)
    return unpack(fmt, data)

def test_char():
    for fmt in "c", "b", "B":
        assert doformat(fmt) == (1, 2, 3.0, 4.0, 5)

def test_int():
    for fmt in "h", "i", "l", "H", "I", "L":
        assert doformat(fmt) == (1, 2, 3.0, 4.0, 5)

def test_float():
    for fmt in "f", "d":
        assert doformat(fmt) == (1, 2, 3.0, 4.0, 5)

