import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    return (u'', len(input))

def bad_encode(input, errors='strict'):
    return (u'', len(input))

codecs.register_error('test.notanencoding', bad_decode)
codecs.register_error('test.notanencoding', bad_encode)

# Test that the error handler is called
try:
    u'\xff'.encode('test.notanencoding')
except UnicodeEncodeError, err:
    if err.object != u'\xff':
        raise AssertionError, "wrong object"
    if err.start != 0:
        raise AssertionError, "wrong start"
    if err.end != 1:
        raise AssertionError, "wrong end"
    if err.reason != 'test.notanencoding':
        raise AssertionError, "wrong reason"
else:
    raise AssertionError, "no exception"

try:
   
