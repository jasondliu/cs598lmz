import _struct
# Test _struct.Struct with native byteorder.
st = _struct.Struct('<I')
# Try various illegal format strings.
for f in ['<dd', '@@', '*4s', '4s*']:
    try:
        _struct.Struct(f)
        raise TestFailed('Illegal format string %r accepted' % f)
    except ValueError:
        pass
    # but '*' should be accepted (for backwards compatibility)
    if f[0] != '*':
        # try it followed by '-', '.', and 'l' (for backwards compatibility)
        for c in '-.l':
            try:
                _struct.Struct(f + c)
                raise TestFailed(('Illegal format string %r'
                                  'accepted followed by %r') % (f, c))
            except ValueError:
                pass
# Try to create a struct without a native format.
ins = _struct.Struct('@i')
