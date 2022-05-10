import _struct
# Test _struct.Struct

# Test that the format string is checked for validity.
try:
    _struct.Struct('x')
except ValueError:
    pass
else:
    print('ValueError not raised')

# Test that the format string can be unicode.
_struct.Struct(u'x')

# Test that the format string can be bytes.
_struct.Struct(b'x')

# Test that the format string can be a subclass of str.
class S(str):
    pass

_struct.Struct(S('x'))

# Test that the format string can be a subclass of bytes.
class B(bytes):
    pass

_struct.Struct(B(b'x'))

# Test that the format string can be a subclass of unicode.
class U(str):
    pass

_struct.Struct(U(u'x'))

# Test that the format string can be an object with a __str__ method.
class X:
    def __str__(self):
        return 'x'

_struct.Struct(X())

# Test that the
