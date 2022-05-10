import _struct
# Test _struct.Struct

def test_struct_pack():
    for code in 'bBhHiIlLqQfd':
        fmt = _struct.Struct(code)
        assert fmt.size == struct.calcsize(code)
        assert fmt.pack(0) == struct.pack(code, 0)
        assert fmt.pack(1) == struct.pack(code, 1)
        assert fmt.pack(-1) == struct.pack(code, -1)
        assert fmt.pack(sys.maxsize) == struct.pack(code, sys.maxsize)
        assert fmt.pack(-sys.maxsize-1) == struct.pack(code, -sys.maxsize-1)
    for code in 'P':
        fmt = _struct.Struct(code)
        assert fmt.size == struct.calcsize(code)
        assert fmt.pack(0) == struct.pack(code, 0)
        assert fmt.pack(1) == struct.pack(code, 1)
        assert fmt.pack(sys.maxsize) == struct.pack(code, sys.maxsize)
    for
