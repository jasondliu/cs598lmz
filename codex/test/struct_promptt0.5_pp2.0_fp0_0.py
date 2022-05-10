import _struct
# Test _struct.Struct

def test_struct():
    struct = _struct.Struct('bBhHiIlLqQfdspP')
    fmt = 'bbHHhhiIlLqQfdfsP'
