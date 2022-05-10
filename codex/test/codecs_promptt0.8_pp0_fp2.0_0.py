import codecs
# Test codecs.register_error()
# This example is from a book.

def my_error_func(exc):
    if isinstance(exc, UnicodeEncodeError):
        # Encoding
        return (u'', exc.end)
    elif isinstance(exc, UnicodeDecodeError):
        # Decoding
        return (u'', exc.end + 1)
    elif isinstance(exc, UnicodeTranslateError):
        # Translating
        return (u'', exc.end + 1)
    else:
        raise TypeError('Could not handle exception')

def my_encode(u):
    """Code to encode unicode string u,
        and return encoded string."""
    pass

def my_decode(b):
    """Code to decode encoded string b,
        and return decoded unicode string."""
    pass

def my_translate(u):
    """Code to translate unicode string u,
        and return translated unicode string."""
    pass

codecs.register_error('my-error-handler', my_error_func)

#
