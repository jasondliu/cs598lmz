import codecs
# Test codecs.register_error()

import codecs

def search_function(encoding):
    return None

codecs.register_error("test.searchfunction", search_function)

import test.search_registry

a, b, c = codecs.lookup_error('test.searchfunction')
print repr(a)
print repr(b)
print repr(c)

# And check that it works correctly

def bad_decoder(input, errors='strict'):
    return None, len(input)

def bad_encoder(input, errors='strict'):
    raise TypeError

codecs.register(bad_decoder)
codecs.register(bad_encoder)

print codecs.decode('abc', 'nonexisting')
try:
    codecs.encode('abc', 'nonexisting')
except TypeError:
    pass
else:
    raise TestFailed

# Test lookup_error()
def strict_handler(exception):
    raise exception

def ignore_handler(exception):
    return (u"
