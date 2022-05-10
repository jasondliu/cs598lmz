import codecs
# Test codecs.register_error() with a name argument:
#
#   1. Try to encode with an unregistered error handler name.
#   2. Register a handler and try to encode again.

import codecs

# Test 1: try to encode with an unregistered error handler name.
try:
    codecs.encode('abc', 'ascii', 'xyzzy')
except LookupError as err:
    print('1. LookupError:', err)
else:
    print('1. No exception raised.')

# Test 2: register an error handler and try to encode again.
def handler(exc):
    return str(exc).encode('ascii'), exc.end

codecs.register_error('xyzzy', handler)
try:
    codecs.encode('abc', 'ascii', 'xyzzy')
except LookupError as err:
    print('2. LookupError:', err)
else:
    print('2. No exception raised.')
