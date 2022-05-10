import codecs
# Test codecs.register_error

import test.test_support

# Register our own error handler
def handler(exception):
    return (u'\ufffd', exception.end)
codecs.register_error('test.ignore', handler)

# Encode a string with our codec
def test(encoding, input):
    # Test both the incremental and stream interfaces
    for func in (lambda: codecs.getincrementalencoder(encoding)(),
                 lambda: codecs.getwriter(encoding)(StringIO())):
        encoder = func()
        for c in input:
            r = encoder.encode(c)
            if c == u'\ufffd':
                if r != u'\ufffd':
                    print 'Unexpected result', repr(r), 'for', repr(c)
            else:
                if r != u'':
                    print 'Unexpected result', repr(r), 'for', repr(c)
        r = encoder.encode(u'', True)
        if r != u'':
            print 'Unexpected result', repr(r), 'for end
