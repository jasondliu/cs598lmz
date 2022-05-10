import _struct
# Test _struct.Struct
_struct.pack('=7b', 1, 1, 2, 3, 5, 8, 13)
_struct.pack('=7b', *range(1, 8))
_struct.pack('=b', 1)
_struct.pack('=b', *range(1, 2))
_struct.pack('=2b', *range(1, 3))

def b(list):
    return [ord(l) for l in list]
def ert(x, y):
    if type(y) is str:
        return x == y
    else:
        return x == ord(y)
def test2(name, format, source, target, **kwd):
    fmt = _struct.Struct(format)
    s =fmt.pack(*source)
    l = list(fmt.unpack(target))
