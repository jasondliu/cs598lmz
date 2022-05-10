import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# This should use the registered search function
assert codecs.lookup('test.searchfunction').name == 'utf-8'

# This should not use the registered search function
