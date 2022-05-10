import codecs
# Test codecs.register_error, then exercise error handlers.
e1 = codecs.lookup_error('ignore')
e2 = codecs.lookup_error('replace')
e3 = codecs.lookup_error('xmlcharrefreplace')
e4 = codecs.lookup_error('backslashreplace')

s = u'ab\xe9'
for enc in ('latin1', 'ascii', 'utf8'):
    t = s.encode(enc, 'ignore')
    print(t)
    t = s.encode(enc, 'replace')
    print(t)
    t = s.encode(enc, 'xmlcharrefreplace')
    print(t)
    t = s.encode(enc, 'backslashreplace')
    print(t)

    # test additional codecs we define for these tests
    def ignore_handler(exception):
        return ('', exception.start + len(exception.object))
    codecs.register_error("ignore_tests", ignore_handler)
    t = s.encode(enc, 'ignore_tests')
