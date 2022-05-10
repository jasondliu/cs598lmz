from _struct import Struct
s = Struct.__new__(Struct)


def test_new_struct():
    assert s.__class__ is Struct
    assert s.__name__ == 'Struct'
    assert s.__doc__ is None
    assert s.format is None
    assert s.size is None
    assert s.alignment is None
    assert s.unpack_from is None
    assert s.pack is None
    assert s.unpack is None


def test_new_struct_no_format():
    with raises(TypeError) as excinfo:
        Struct()
    assert str(excinfo.value) == 'Struct() missing required argument \'format\''


def test_new_struct_with_format():
    s = Struct('i')
    assert s.__class__ is Struct
    assert s.__name__ == 'Struct'
    assert s.__doc__ is None
    assert s.format == 'i'
    assert s.size == 4
    assert s.alignment == 4
    assert s.unpack_from is None
    assert s.pack is None
    assert s.unpack is None


def
