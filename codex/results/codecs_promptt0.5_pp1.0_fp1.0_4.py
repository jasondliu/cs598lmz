import codecs
# Test codecs.register_error()

#------------------------------------------------------------------------------

def test_register_error():
    # Testing codecs.register_error
    import codecs
    import string
    errors = []

    def handler(exception):
        errors.append(exception.__class__)
        return ('X', exception.end)

    codecs.register_error('test.codec', handler)

    # Unencodable character
    s = 'abc\xFFdef'
    u = s.decode('ascii', 'test.codec')
    assert u == 'abcXdef'
    assert errors == [UnicodeEncodeError]
    errors = []

    # Invalid byte sequence
    s = 'abc\xFFdef'
    u = s.decode('ascii', 'test.codec')
    assert u == 'abcXdef'
    assert errors == [UnicodeDecodeError]
    errors = []

    # Truncated byte sequence
    s = 'abc\xFF'
    u = s.decode('ascii', 'test.codec')
   
