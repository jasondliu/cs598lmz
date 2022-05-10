import _struct
# Test _struct.Struct.format_size()
def test_struct_format_size():
    fmt = '@ 2x 3p 2h 5l 2L 3q 2Q 3P 3n 2N 3i 2I 3I 2f 3d 2F 3D 2g 3G 2e 3E 2E 3c 2s 3w 2S 3b 2B 3B 2t 3T 2u 3H 2h 3k 2i 3K 2l 3L 2q 3Q 2Q 3N 2P 3o 2O 3O 2x'
    s = _struct.Struct(fmt)
    assert s.format_size() == 8 + 3*_struct.calcsize('P') + 3*_struct.calcsize('n') + 3*_struct.calcsize('i') + 2*_struct.calcsize('I') + 3*_struct.calcsize('f') + 2*_struct.calcsize('d') + 3*_struct.calcsize('g') + 2*_struct.calcsize('e') + 3*_struct.calcsize('c') + 3*_struct.cal
