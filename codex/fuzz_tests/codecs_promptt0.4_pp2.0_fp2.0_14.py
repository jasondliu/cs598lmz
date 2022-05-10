import codecs
# Test codecs.register_error()

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.replace', replace_error)

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    print '\n*** Encoding:', encoding
    for input in ['abc', '\x80', '\xff', '\u0100', '\udc80']:
        print 'Input:', repr(input)
        print 'Output:', repr(input.encode(encoding, 'test.replace'))

def xmlcharrefreplace_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        s = []
        for c in exc.object[exc.start:exc.end]:
            s.append(u'&#%d;' % ord(c))
        return (u
