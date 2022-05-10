import codecs
# Test codecs.register_error()
def test(encoding):
    print '%s:' % encoding,
    try:
        ustring = u'\u0080'
        print repr(ustring.encode(encoding)),
        codecs.register_error(encoding, lambda x: 'E')
        print repr(ustring.encode(encoding)),
        codecs.register_error(encoding, 'replace')
        print repr(ustring.encode(encoding)),
        codecs.register_error(encoding, 'ignore')
        print repr(ustring.encode(encoding))
    except UnicodeError, detail:
        print str(detail)
test('ascii')
test('iso8859-1')
test('utf-8')
test('unicode-internal')
