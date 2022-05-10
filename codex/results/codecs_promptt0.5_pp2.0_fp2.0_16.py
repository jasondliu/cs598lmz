import codecs
# Test codecs.register_error()
def test_register_error():
    # Encoding
    assert codecs.register_error('strict', lambda x: (u'', x + 1))
    assert codecs.register_error('ignore', lambda x: (u'', x + 2))
    assert codecs.register_error('replace', lambda x: (u'', x + 3))
    assert codecs.register_error('xmlcharrefreplace', lambda x: (u'', x + 4))
    assert codecs.register_error('backslashreplace', lambda x: (u'', x + 5))

    # Decoding
    assert codecs.register_error('strict', lambda x: (u'', x + 6))
    assert codecs.register_error('ignore', lambda x: (u'', x + 7))
    assert codecs.register_error('replace', lambda x: (u'', x + 8))
    assert codecs.register_error('xmlcharrefreplace', lambda x: (u'', x + 9))
    assert codecs.register_error('backslashreplace', lambda x:
