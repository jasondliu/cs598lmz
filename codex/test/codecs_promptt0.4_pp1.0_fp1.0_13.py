import codecs
# Test codecs.register_error

import codecs

def search_function(encoding):
    if encoding != 'test.searchfunction':
        return None
    return codecs.lookup('utf-8')

codecs.register(search_function)

u = u'\u3042'
assert codecs.encode(u, 'test.searchfunction') == u.encode('utf-8')

# Test codecs.register_error

def ignore_errors(error):
    print('ignore_errors called with %r' % error)
    return (u'', error.end)

codecs.register_error('ignore', ignore_errors)

# Test codecs.lookup

assert codecs.lookup('ascii') is codecs.lookup('ascii')
