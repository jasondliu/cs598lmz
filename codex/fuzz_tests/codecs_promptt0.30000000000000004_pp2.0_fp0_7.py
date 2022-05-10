import codecs
# Test codecs.register_error

# This test is for the case where the error handler is a string
# and the string is not a valid error handler name.

import codecs

def search_function(encoding):
    if encoding == 'test.search.failure':
        return None
    return None

codecs.register(search_function)

def test():
    try:
        codecs.lookup('test.search.failure')
    except LookupError:
        pass
    else:
        raise AssertionError, "lookup should have failed"
    try:
        codecs.lookup_error('test.search.failure')
    except LookupError:
        pass
    else:
        raise AssertionError, "lookup_error should have failed"
    try:
        codecs.lookup_error('test.search.failure', 'strict')
    except LookupError:
        pass
    else:
        raise AssertionError, "lookup_error should have failed"

test()
