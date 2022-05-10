import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# This should use the registered search function
s = '\xe9'
u = s.decode('test.searchfunction')
print repr(u)

# This should use the builtin search function
s = '\xe9'
u = s.decode('test.searchfunction2')
print repr(u)
