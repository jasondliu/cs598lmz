import _struct
# Test _struct.Struct, _struct.unpack_from(), _struct.calcsize()

def test(fmt):
    s = _struct.Struct(fmt)
    res = s.unpack_from
    slen = s.size
    fmt2 = s.format
    return res, slen, fmt2

res, slen, fmt2 = test('hi')
data = 'abc' + 'x' * 6
try:
    res(data)
except TypeError:
    pass
