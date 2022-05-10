import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

def test_register_error(encoding):
    # Test codecs.register_error
    try:
        codecs.lookup_error('strict')
    except LookupError:
        pass
    else:
        raise TestFailed('lookup_error() found registered "strict" error handler')

    codecs.register_error('strict', codecs.strict_errors)
    try:
        codecs.lookup_error('strict')
    except LookupError:
        raise TestFailed('lookup_error() did not find registered "strict" error handler')

    # Test whether the registered error handler is actually used
    s = u'\udcff'
    try:
        s.encode(encoding)
    except UnicodeEncodeError:
        pass
    else:
        raise TestFailed('encoding did not raise UnicodeEncodeError')

