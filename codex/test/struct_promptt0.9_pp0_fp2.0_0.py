import _struct
# Test _struct.Struct's slice, unpack and pack methods
# The slice() method is just a convenience:
with open(testfn, 'wb') as f:
    f.write(b"a\x00\xc0b\xb1\x03c\x13\x02\xd0\x08")
s = _struct.Struct('h2s 3x 8s x h')
for p, v in enumerate([
    ((6, ('b', '\xb1\x03')), b'\0\xc0b\xb1\x03c\x13\x02\xd0'),
    ((1,), b'a\x00'),
    ((4, ('\x13\x02',)), b'ab\xb1\x03\x13\x02\xd0'),
]):
    res = s.unpack_from(f.getvalue(), *p)
    with open(testfn, 'rb') as f:
        fp = s.pack(*v)
