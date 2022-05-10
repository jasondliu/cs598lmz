import io
# Test io.RawIOBase behavior

import _io

# Encoding shouldn't be specified
try:
    _io.BytesIO(u'a', 'latin1')
except TypeError:
    pass
else:
    print('1..0 # SKIP bytes and bytearray methods must fail without encoding argument')

# Test readinto from array on empty object
a = bytearray(b'abcdef')
f = _io.BytesIO(b'')
f.readinto(a)
print(a.__repr__(), '2')
print('2')

# Test readinto from array from partially-filled object
a = bytearray(b'abcdef')
f = _io.BytesIO(b'xyz')
f.readinto(a)
print(a.__repr__(), '3')
print('3')

# Test readinto from array from fully-filled object
a = bytearray(6)
f = _io.BytesIO(b'xyz123')
f.readinto(a)
print(a.__repr__(), '4
