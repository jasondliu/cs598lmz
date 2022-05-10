import codecs
# Test codecs.register_error()

def bad_unicode_error_handler(exc):
    print(exc)
    return (b'\x00', exc.end)

codecs.register_error('test', bad_unicode_error_handler)

encoding = 'ascii'
encoded_text = b'abc\x00\xe9'
print(encoded_text.decode(encoding, 'test'))

print(encoded_text.decode(encoding, 'strict'))
# Test UnicodeEncodeError exception

def bad_unicode_encode_error_handler(exc):
    if isinstance(exc, UnicodeEncodeError):
        # The text is longer than the max size we are willing to accept.
        # We cut off the text.
        print(exc)
        if exc.end > exc.start + 10:
            exc.end = exc.start + 10
        return (u'', exc.end)
    else:
        # Some other error occurred:
        return codecs.strict_errors(exc)

codecs
