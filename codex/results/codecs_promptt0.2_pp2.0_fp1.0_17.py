import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

# Test that the error handler is called
try:
    codecs.decode('\xff', 'ascii', 'my_error')
except UnicodeDecodeError:
    pass
else:
    print('UnicodeDecodeError not raised')

# Test that the error handler is called
try:
    codecs.encode('\u1234', 'ascii', 'my_error')
except UnicodeEncodeError:
    pass
else:
    print('UnicodeEncodeError not raised')

# Test that the error handler is called
try:
    codecs.escape_decode(b'\xff')
except UnicodeDecodeError:
    pass
else:
    print('UnicodeDecodeError not raised')

# Test that the error handler is called
try:
    codecs.escape_encode(u'\u1234')

