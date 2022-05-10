import codecs
# Test codecs.register_error
def test_register_error():
    def handler(exception):
        return (u'', exception.end)
    codecs.register_error('test.ignore', handler)
    assert codecs.lookup_error('test.ignore') is handler
    try:
        codecs.register_error('test.ignore', handler)
    except ValueError:
        pass
    else:
        raise AssertionError
    codecs.register_error('test.ignore', None)
    assert codecs.lookup_error('test.ignore') is None
    try:
        codecs.register_error('test.ignore', None)
    except ValueError:
        pass
    else:
        raise AssertionError
    try:
        codecs.register_error('test.ignore', 'spam')
    except TypeError:
        pass
    else:
        raise AssertionError
    try:
        codecs.register_error(42, handler)
    except TypeError:
        pass
    else:
        raise AssertionError
