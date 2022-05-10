import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return '<ERROR>', exception.end

codecs.register_error('my_error', my_error_handler)

utf8 = codecs.lookup('utf-8')

assert utf8.encode('\x80', 'my_error') == ('<ERROR>', 1)
assert utf8.decode('\xc2', 'my_error') == ('<ERROR>', 1)

# Test codecs.register_error() with a string

import codecs

def my_error_handler(exception):
    return '<ERROR>', exception.end

codecs.register_error('my_error', '<ERROR>')

utf8 = codecs.lookup('utf-8')

assert utf8.encode('\x80', 'my_error') == ('<ERROR>', 1)
assert utf8.decode('\xc2', 'my_error') == ('<ERROR>', 1)

# Test codecs.register_
