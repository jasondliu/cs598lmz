import _struct
# Test _struct.Struct.

def test_struct(tpl, bigendian):
    for format, setargs, exp in tpl:
        if bigendian:
            format = '>' + format
        else:
            format = '<' + format
        strct = _struct.Struct(format)
        # Test __doc__
        doc = strct.__doc__
        if not doc.startswith(format + '\n\n'):
            raise ValueError('__doc__=%a does not start with %a' % (doc,
                             format + '\n\n'))
        # Test format
        if strct.format != format:
            raise ValueError('format=%a, expected %a' % (strct.format, format))
        # Test size
        size = strct.size
        if not isinstance(size, int):
            raise TypeError('size=%a, expected int' % size)
        # Test pack
        args = setargs()
        packed = strct.pack(*args)
        if len(packed) != size:
            raise
