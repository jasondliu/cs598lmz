import codecs
# Test codecs.register_error()

def handler(exc):
    if issubclass(exc, UnicodeEncodeError):
        return (u'REPLACEMENT CHARACTER', exc.end)
    if issubclass(exc, UnicodeDecodeError):
        return (u'REPLACEMENT CHARACTER', exc.start + 1)
    raise TypeError("don't know how to handle %r" % exc)

for encoding in ['ascii', 'latin-1', 'utf-16', 'utf-8']:
    print 'Testing with %r:' % encoding
    print codecs.register_error(handler, encoding)
    try:
        print 'U+fffe in %r -> %r' % (encoding, u'\ufffe'.encode(encoding, 'strict'))
    except UnicodeEncodeError, e:
        print 'UnicodeEncodeError:', e.encode('ascii', 'backslashreplace')
    try:
        print 'b\'\xff\' in %r -> %r' % (encoding, '\xff'.decode(enc
