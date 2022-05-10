import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('ascii')
    return None

codecs.register(search_function)

# Test codecs.lookup

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('ascii')
    return None

codecs.register(search_function)

# Test codecs.lookup_error

import codecs

