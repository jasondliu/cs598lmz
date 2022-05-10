import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')

codecs.register(search_function)

# Test codecs.lookup()

def test(encoding):
    try:
        codecs.lookup(encoding)
    except LookupError:
        print('ERROR:', encoding)
    else:
        print('OK:', encoding)

test('test.searchfunction')
test('test.searchfunction2')

# Test codecs.lookup_error()

def handler(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('UnicodeDecodeError:', exc.object, exc.start, exc.end, exc.reason)
        return ('', exc.end)
    raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.lookuperror', handler)

