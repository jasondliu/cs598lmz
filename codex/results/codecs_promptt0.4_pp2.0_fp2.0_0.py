import codecs
# Test codecs.register_error
import codecs

def handler(exception):
    """Handle UnicodeEncodeError by replacing unencodable characters."""
    return (u'X', exception.end)

codecs.register_error('test.replace_with_X', handler)

# Test that the error handler is used
s = u'abc\uFFFDdef'
try:
    s.encode('ascii', 'test.replace_with_X')
except UnicodeEncodeError:
    pass
else:
    print('UnicodeEncodeError not raised')

# Test that the error handler is not used if the error handler name is not
# specified
s = u'abc\uFFFDdef'
try:
    s.encode('ascii')
except UnicodeEncodeError:
    pass
else:
    print('UnicodeEncodeError not raised')

# Test that the error handler is not used if the error handler name is
# specified but not registered
s = u'abc\uFFFDdef'
try:
    s.encode('ascii', '
