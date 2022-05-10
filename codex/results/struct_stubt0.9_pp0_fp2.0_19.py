from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()

_fmt = self.format
if self._size is not None:
    if (flags & _IEEE754_MASK):
        # If a struct is not compiled we just set the code and size.
        # We don't check the sizes because they could also be
        # arbitrary strings.
        self.format = '<'
        _fmt = ''
    else:
        raise error('Non-IEEE floating point formats are not supported')

# If you want to see the method resolution order, uncomment this print
print(Struct.mro())

s.format = _fmt
