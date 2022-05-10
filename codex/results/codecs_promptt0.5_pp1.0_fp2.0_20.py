import codecs
# Test codecs.register_error()
def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    encoding = 'ascii'
    return codecs.lookup(encoding)

codecs.register(search_function)

def test():
    # Test normal operation
    assert codecs.encode('abc', 'test.searchfunction') == b'abc'
    assert codecs.encode('abc', 'test.searchfunction', 'xmlcharrefreplace') == b'abc'

    # Test with an error handler
    assert codecs.encode('\u1234', 'test.searchfunction', 'ignore') == b''

    # Test with an error handler that raises an exception
    raises(UnicodeEncodeError, codecs.encode, '\u1234', 'test.searchfunction', 'strict')

    # Test with an unknown error handler
    raises(LookupError, codecs.encode, 'abc', 'test.searchfunction', '__OINK__')

class IncrementalEncoder(codecs.IncrementalEncoder):
   
