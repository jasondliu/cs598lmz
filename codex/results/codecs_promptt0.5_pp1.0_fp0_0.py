import codecs
# Test codecs.register_error

def test_register_error():
    # Initialize the module
    reload(codecs)
    # Save the state of the current error handlers
    default_error = codecs.lookup_error('strict')
    xmlcharrefreplace_error = codecs.lookup_error('xmlcharrefreplace')
    ignore_error = codecs.lookup_error('ignore')
    replace_error = codecs.lookup_error('replace')
    xmlcharnamereplace_error = codecs.lookup_error('namereplace')
    backslashreplace_error = codecs.lookup_error('backslashreplace')

    # Test the default error handlers
    for c in [u'\u1234', u'\ufffe', u'\udcfe', u'\ud800\udc00']:
        assert default_error(UnicodeEncodeError('ascii', c, 0, 1, 'ouch')) == (
            u'\\ud834\\udc4d', 4)
        assert xmlcharrefreplace_error(
            UnicodeEncode
