import codecs
# Test codecs.register_error for codecs that use the surrogateescape error
# handler.
import _testcapi
import sys

# Test surrogateescape error handler
def test_surrogateescape():
    # Test the surrogateescape error handler
    # This error handler is only available on systems that use UTF-8 locales
    # (e.g. Linux)
    if sys.platform == 'win32':
        return

    # Test surrogateescape error handler
    # Encode a string with a character that can't be encoded
    s = 'abc\uDC80def'
    try:
        b = s.encode('ascii')
    except UnicodeEncodeError:
        pass
    else:
        raise Exception('encoding should have failed')

    # Register the error handler
    codecs.register_error('test.surrogateescape', codecs.surrogateescape_error)

    # Encode again. This time, the encoding should succeed, but the
    # character that can't be encoded will be replaced by a character
    # in the range U+DC80-U+DCFF.
    b = s.
