import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding == 'test.searchfunction':
        return codecs.lookup('utf-8')
    return None

codecs.register(search_function)

# Test the search function
u = u'\u20ac'
for encoding in ('test.searchfunction', 'utf-8'):
    assert codecs.encode(u, encoding) == '\xe2\x82\xac'
    assert codecs.decode('\xe2\x82\xac', encoding) == u

# Test the error handler
def error_handler(exception):
    return (u'', exception.end)

codecs.register_error('test.errorhandler', error_handler)

assert codecs.decode('\xff', 'ascii', 'test.errorhandler') == u''

# Test the incremental encoder
def encode(input, errors='strict'):
    return u''.join(input), len(input)

codecs.register_error('test.incremental
