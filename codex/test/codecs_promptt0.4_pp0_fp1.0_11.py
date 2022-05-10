import codecs
# Test codecs.register_error()

import codecs

# This codec uses surrogateescape error handling, but we register a
# different error handler for it

def search_function(encoding):
    if encoding == 'test.surrogateescape':
        return codecs.lookup('utf-8')

codecs.register(search_function)

def my_surrogateescape_handler(exc):
    return (u'\ufffd', exc.start+1)

codecs.register_error('test.surrogateescape', my_surrogateescape_handler)

utf8_data = b'\xed\xa0\x80' # U+D800 encoded in UTF-8

# First, try without registering the error handler
