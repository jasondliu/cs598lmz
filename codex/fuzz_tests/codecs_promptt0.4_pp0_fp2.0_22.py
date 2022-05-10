import codecs
# Test codecs.register_error
import _codecs

def codec_error_handler(exception):
    if isinstance(exception, UnicodeDecodeError):
        return u'', exception.end
    elif isinstance(exception, UnicodeEncodeError):
        return u'', exception.end
    elif isinstance(exception, UnicodeTranslateError):
        return u'', exception.end
    else:
        raise TypeError("don't know how to handle %r" % exception)

# Test codecs.register_error
def test_register_error():
    # Test UnicodeEncodeError handler
    codecs.register_error("test.unicodeencodeerror", codec_error_handler)
    try:
        u'\ud800'.encode("ascii", "test.unicodeencodeerror")
    except UnicodeEncodeError:
        raise TestFailed("encoding with test.unicodeencodeerror failed")

    # Test UnicodeDecodeError handler
    codecs.register_error("test.unicodedecodeerror", codec_error_handler)
    try:
        '
