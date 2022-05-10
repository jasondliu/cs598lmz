import codecs
# Test codecs.register_error by passing in a funny UnicodeError subclass and
# providing an error handler.
class FunnyUnicodeError(UnicodeError):
    """subclass of UnicodeError for testing purposes"""
    pass
class FunnyUnicodeDecodeError(UnicodeDecodeError):
    """subclass of UnicodeDecodeError for testing purposes"""
    pass


def handler(e):
    return ('spam', e.end)
FUNNY_ERROR = FunnyUnicodeError('spam', 'eggs', 42, 1337.0)
