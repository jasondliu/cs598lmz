import _struct
# Test _struct.Struct for special characters and invalid names
for name in (b'', b'a ', b'a\nb', b'a\x00b'):
    try:
        struct.Struct(name)
    except ValueError:
        pass
    else:
        raise SystemExit('_struct.Struct did not raise ValueError')
for name in ('101', 'a+b', 'sTrue', 'sFalse', 'sNone'):
    try:
        struct.Struct(name)
    except ValueError:
        pass
    else:
        raise SystemExit('_struct.Struct did not raise ValueError')
