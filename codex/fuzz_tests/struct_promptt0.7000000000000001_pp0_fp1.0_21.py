import _struct
# Test _struct.Struct instances.

# _struct.Struct() should not be callable.

try:
    w = _struct.Struct()
except TypeError:
    pass
else:
    raise TestFailed, "expected TypeError"

# _struct.Struct(format) should be callable.

def test_single_format(format):
    s = _struct.Struct(format)
    data = _struct.pack(format, 1)
    try:
        s.pack()
    except TypeError:
        pass
    else:
        raise TestFailed, "expected TypeError"
    try:
        s.pack(1, 2, 3)
    except TypeError:
        pass
    else:
        raise TestFailed, "expected TypeError"
    try:
        s.unpack()
    except TypeError:
        pass
    else:
        raise TestFailed, "expected TypeError"
    try:
        s.unpack(data, 1, 2, 3)
    except TypeError:
        pass
    else:
        raise TestFailed, "expected Type
