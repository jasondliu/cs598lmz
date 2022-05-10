import _struct
# Test _struct.Struct

# Test the alignment of the struct
def test_alignment():
    assert _struct.calcsize("x") == 1
    assert _struct.calcsize("xx") == 2
    assert _struct.calcsize("xxi") == 8
    assert _struct.calcsize("xxix") == 12
    assert _struct.calcsize("xxixi") == 16
    assert _struct.calcsize("xxixix") == 20
    assert _struct.calcsize("xxixixi") == 24
    assert _struct.calcsize("xxixixix") == 32
    assert _struct.calcsize("xxixixixi") == 40
    assert _struct.calcsize("xxixixixix") == 48
    assert _struct.calcsize("xxixixixixi") == 56
    assert _struct.calcsize("xxixixixixix") == 64
    assert _struct.calcsize("xxixixixixixi") == 72
    assert _struct.calcsize("xxixixixixixix") == 80
   
