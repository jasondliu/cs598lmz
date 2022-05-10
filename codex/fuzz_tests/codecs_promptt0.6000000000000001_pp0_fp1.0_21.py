import codecs
# Test codecs.register_error()

def codec_error_handler(exception):
    print 'Handling exception:', exception
    return (u'', exception.end)

def test_codec_error_handler():
    codecs.register_error('test.codec', codec_error_handler)
    s = '\xff'
    try:
        u = s.decode('ascii', 'test.codec')
    except UnicodeDecodeError, detail:
        print 'UnicodeDecodeError:', detail
        print 'start:', detail.start
        print 'end:', detail.end
        print 'object:', repr(detail.object)
        print 'reason:', detail.reason
        print 'encoding:', detail.encoding

# codecs

def test_codecs():
    s = 'abc\x80\u0100'
    print repr(s)
    u = s.decode('latin1')
    print repr(u)
    s = u.encode('raw_unicode_escape')
    print repr(s)
    u
