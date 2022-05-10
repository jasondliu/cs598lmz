import codecs
# Test codecs.register_error

def codec_test(testname, encoding, input, errors='strict'):
    print '%s:' % testname
    try:
        decoded = codecs.utf_8_decode(input, errors)
    except Exception, why:
        print '    ERROR:', why
    else:
        encoded = codecs.utf_8_encode(decoded[0], errors)
        print '   ', repr(input), '->',
        print repr(decoded[0]), '->',
        print repr(encoded[0]),
        if encoded[0] != input:
            print 'NO MATCH',
        else:
            print
    print

codec_test('no error handler', 'utf-8',
           "\xed\xb2\x80"
           )

codec_test('ignore', 'utf-8',
           "\xed\xb2\x80",
           'ignore'
           )

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        x = unicode('\ufffd
