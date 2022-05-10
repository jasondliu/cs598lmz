import codecs
# Test codecs.register_error()

def bad_unicode_error_handler(exc):
    print(exc)
    return (b'\x00', exc.end)

codecs.register_error('test', bad_unicode_error_handler)

encoding = 'ascii'
encoded_text = b'abc\x00\xe9'
