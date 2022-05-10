import _struct
# Test _struct.Struct

def test_struct_error():
    try:
        _struct.Struct('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct() did not raise TypeError'

def test_struct_pack():
    s = _struct.Struct('i')
    try:
        s.pack()
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct().pack() did not raise TypeError'
    try:
        s.pack(1, 2)
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct().pack() did not raise TypeError'
    try:
        s.pack(1.0)
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct().pack() did not raise TypeError'
    try:
        s.pack('abc')
    except TypeError:
        pass
    else:
        raise TestFailed, '_struct.Struct().pack() did not
