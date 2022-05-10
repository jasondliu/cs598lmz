import _struct
# Test _struct.Struct() and .pack()
for fmt in ['p']:
    for n in range(500):
        s = _struct.Struct(fmt)
        try:
            s.pack(n)
        except Exception:
            print('Format %r' % (fmt,), end=' ')
            print('packed %r' % (n,), end=' ')
            print('and raised %r' % (sys.exc_info()[1],))
# Test _struct.Struct() and .unpack()
for fmt in ['p']:
    for n in range(500):
        s = _struct.Struct(fmt)
        try:
            s.unpack(s.pack(n))
        except Exception:
            print('Format %r' % (fmt,), end=' ')
            print('packed %r' % (n,), end=' ')
            print('and raised %r' % (sys.exc_info()[1],))
# Test _struct.Struct() and .pack_into()
for fmt in ['p']:
    for n in range(
