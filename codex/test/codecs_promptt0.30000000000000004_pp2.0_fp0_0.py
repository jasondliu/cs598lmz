import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Now the encoding should be available
print(codecs.encode('abc', 'test.searchfunction'))

# Test codecs.lookup()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Now the encoding should be available
print(codecs.lookup('test.searchfunction').name)

# Test codecs.lookup_error()

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Now the encoding should be available
