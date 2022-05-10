import codecs
# Test codecs.register_error

# This test is in Lib/test/test_codecs.py
def test_register_error():
    def custom_error_handler(exception):
        return (u'', exception.end)

    codecs.register_error('test.custom_error_handler', custom_error_handler)
    s = u'\uFFFEabc'
    try:
        s.encode('ascii', 'test.custom_error_handler')
    except UnicodeEncodeError:
        pass
    else:
        self.fail('encoding with custom_error_handler must fail')

# Test codecs.lookup

# This test is in Lib/test/test_codecs.py
def test_lookup():
    # check that we can still lookup the builtin UTF8 codec
    utf8 = codecs.lookup('utf8')
    s = u'\xfc'
    try:
        utf8.encode(s, 'strict')
    except UnicodeEncodeError:
        pass
