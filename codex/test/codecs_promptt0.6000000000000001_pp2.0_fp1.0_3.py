import codecs
# Test codecs.register_error 
# See http://bugs.python.org/issue8257 for details

def test_register_error():
    def handler(exception):
        return ('', exception.end)

    codecs.register_error('test.my_error', handler)
    s = u'\u3042\u3044'
    e = UnicodeEncodeError('ascii', s, 0, 1, 'ouch')
    r, size = codecs.lookup_error('test.my_error')(e)
    assert r == (u'', 1)


def test_register_error():
    def handler(exception):
        return (u'', exception.end)

    codecs.register_error('test.my_error', handler)
    s = '\xe3\x81\x82\xe3\x81\x84'
    e = UnicodeDecodeError('ascii', s, 0, 1, 'ouch')
    r, size = codecs.lookup_error('test.my_error')(e)
