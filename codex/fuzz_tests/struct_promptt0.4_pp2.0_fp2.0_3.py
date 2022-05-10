import _struct
# Test _struct.Struct with all formats

# Test _struct.Struct with all formats

import _struct

def test_struct():
    # Test _struct.Struct with all formats
    for code in _struct.__dict__:
        if code[0] in 'bBhHiIlLqQfd':
            format = '!' + code
            size = _struct.calcsize(format)
            if size == 0:
                continue
            s = _struct.Struct(format)
            f = getattr(s, 'pack_into' if hasattr(s, 'pack_into') else 'pack')
            b = bytearray(size)
            f(b, 0, 0)
            f(b, 0, 1)
            f(b, 0, -1)
            f(b, 0, 2)
            f(b, 0, -2)
            f(b, 0, 2**(8*size-1)-1)
            f(b, 0, -2**(8*size-1))
            f(b, 0, 2**(8*size-1))
