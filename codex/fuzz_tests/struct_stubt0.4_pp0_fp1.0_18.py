from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 5
s.pack = lambda x: x
s.unpack = lambda x: x

def test_struct():
    assert struct.pack('<i', 1) == s.pack(1)
    assert struct.unpack('<i', s.pack(1)) == s.unpack(1)
    assert struct.calcsize('<i') == s.size()

def test_struct_nested():
    assert struct.pack('<ii', 1, 2) == s.pack((1, 2))
    assert struct.unpack('<ii', s.pack((1, 2))) == s.unpack((1, 2))
    assert struct.calcsize('<ii') == s.size()

def test_struct_nested_nested():
    assert struct.pack('<iii', 1, 2, 3) == s.pack(((1, 2), 3))
    assert struct.unpack('<iii', s.pack(((1, 2), 3))) == s.unpack(((1, 2), 3))
    assert struct.
