import _struct
# Test _struct.Struct with big endian.
def pack(*args):
    return struct.pack(endian + 'i', *args)
S = _struct.Struct(endian + 'i')
for args in [[1], [1] * 2, [1] * 10, [1] * 100, [1] * 1000, [1] * 10000]:
    s = S.pack(*args)
    t = pack(*args)
    assert s == t, (s, t)

def unpack(s):
    return struct.unpack(endian + 'i' * (len(s) // 4), s)
for args in [[1], [1] * 2, [1] * 10, [1] * 100, [1] * 1000, [1] * 10000]:
    s = pack(*args)
    t = S.unpack(s)
    assert t == args, (t, args)
    t = unpack(s)
    assert t == args, (t, args)

# Test _struct.Struct with little endian.
