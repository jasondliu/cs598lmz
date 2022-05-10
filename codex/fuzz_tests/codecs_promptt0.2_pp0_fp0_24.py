import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Test that the search function is called
u = u'\u3042'
assert codecs.encode(u, 'test.searchfunction') == '\xe3\x81\x82'

# Test that the search function is called for the error handler
def error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.searchfunction', error_handler)

assert codecs.decode('\xff', 'test.searchfunction', 'replace') == u''

# Test that the search function is called for the incremental encoder
def encode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.searchfunction', encode)

assert codecs.encode(u'', 'test.searchfunction') == u
