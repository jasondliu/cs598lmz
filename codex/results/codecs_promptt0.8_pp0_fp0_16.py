import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'@', exception.start + 1)

def reader(stream, errors='strict'):
    return codecs.StreamReader(stream, errors, handler)

codecs.register_error(name='test.raise_on_xyz', handler=handler)

for encoding in ['test.raise_on_xyz']:
    for s in [b'abcdefghi', b'abc\x80def', b'abc\x80\x80def']:
        print(s, encoding)
        t = s.decode(encoding)
        print(' ', t, t.encode(encoding))
