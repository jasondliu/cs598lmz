import _struct
# Test _struct.Struct

def test_sizeof():
    s = _struct.Struct('h')
    assert s.size == 2

    s = _struct.Struct('hil') # subclasses must have an overriden size attribute
    assert s.size == 9

def test_pack_unpack():
    s = _struct.Struct('3h')
    packed = s.pack(1, 2, 3)
    assert s.unpack(packed) == (1, 2, 3)

def test_unpack_from():
    s = _struct.Struct('3h')
    packed = s.pack(1, 2, 3)
    assert s.unpack_from(packed) == (1, 2, 3)
    assert s.unpack_from(packed, 1) == (2, 3, 0)

def test_iter_unpack():
    s = _struct.Struct('3h')
    packed = s.pack(1, 2, 3)
    iterator = s.iter_unpack(packed)
    assert iterator.__next__() == 1
    assert iterator.__
