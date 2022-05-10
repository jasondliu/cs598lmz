import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Test that the search function is called
assert codecs.lookup('test.searchfunction') is codecs.lookup('utf-8')

# Test that the search function is called only once
assert codecs.lookup('test.searchfunction') is codecs.lookup('test.searchfunction')

# Test that the search function is called only once
assert codecs.lookup('test.searchfunction') is codecs.lookup('test.searchfunction')

# Test that the search function is called only once
assert codecs.lookup('test.searchfunction') is codecs.lookup('test.searchfunction')

# Test that the search function is called only once
assert codecs.lookup('test.searchfunction') is codecs.lookup('test.searchfunction')

# Test that the search function is called only once
assert codecs.look
