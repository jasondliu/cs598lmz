import codecs
# Test codecs.register_error
def test_register_error():
    def my_lookup(errors):
        return codecs.lookup_error(errors)
    codecs.register_error('my_lookup', my_lookup)
    assert codecs.lookup_error('my_lookup') is my_lookup
    try:
        codecs.register_error('my_lookup', None)
        raise Exception('Expected TypeError')
    except TypeError:
        pass
    codecs.register_error('my_lookup', lambda errors: None)
    assert codecs.lookup_error('my_lookup') is None

# Test codecs.lookup_error
def test_lookup_error():
    try:
        codecs.lookup_error('__does_not_exist__')
        raise Exception('Expected LookupError')
    except LookupError:
        pass
    try:
        codecs.lookup_error(None)
        raise Exception('Expected LookupError')
    except LookupError:
        pass
    assert codecs.lookup
