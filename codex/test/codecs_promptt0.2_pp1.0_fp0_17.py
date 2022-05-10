import codecs
# Test codecs.register_error

# This test is for the case where the error handler is a function
# that takes a UnicodeDecodeError as its argument.

def handler(e):
    return (u'\ufffd', e.end)

codecs.register_error('test.unicode_decode_error', handler)

