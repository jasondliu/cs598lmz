import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('my_error', my_error_handler)

codecs.decode('abc\x80def', 'ascii', 'my_error')

# Test codecs.lookup_error

import codecs

def my_error_handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('my_error', my_error_handler)

codecs.lookup_error('my_error')

# Test codecs.lookup_error with unknown error handler

import codecs

try:
    codecs.lookup_error('my_error')
except LookupError:
    print('LookupError')

# Test codecs.lookup_error with non-string error handler

import codecs

try:
    codecs.lookup_error(42)
except TypeError:
    print
