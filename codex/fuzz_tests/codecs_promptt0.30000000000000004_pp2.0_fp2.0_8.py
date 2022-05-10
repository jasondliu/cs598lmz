import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

utf8_decoder = codecs.getincrementaldecoder('utf-8')()
utf8_decoder.set_error_handler('my_error')

utf8_decoder.decode('\x80')

utf8_decoder.decode('\xc0')

utf8_decoder.decode('\xc0\x80')

utf8_decoder.decode('\xc0\x80', final=True)

# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'', exception.end)

codecs.register_error('my_error', my_error_handler)

utf8_decoder = codecs.getincrementaldecoder('utf-8')()
utf8_decoder.set_error_handler('my
