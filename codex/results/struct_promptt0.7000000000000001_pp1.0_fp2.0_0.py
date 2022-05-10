import _struct
# Test _struct.Struct()
def test_struct_ctor():
    try:
        _struct.Struct('c')
    except TypeError:
        pass
    else:
        fail("_struct.Struct() doesn't raise TypeError when given too few arguments")

    try:
        _struct.Struct('c', 'extra argument')
    except TypeError:
        pass
    else:
        fail("_struct.Struct() doesn't raise TypeError when given too many arguments")

    try:
        _struct.Struct(0)
    except TypeError:
        pass
    else:
        fail("_struct.Struct() doesn't raise TypeError when given invalid arguments")

    try:
        _struct.Struct('c', 0)
    except TypeError:
        pass
    else:
        fail("_struct.Struct() doesn't raise TypeError when given invalid arguments")

    try:
        _struct.Struct('c', 0, 0)
    except TypeError:
        pass
    else:
        fail("_struct.Struct() doesn't raise TypeError when given invalid arguments")

    try:
        _struct.Struct
