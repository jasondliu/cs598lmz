import codecs
# Test codecs.register_error
#
# This test is a bit lame, but it's better than nothing.

import codecs
import test.support

def check_register_error(encoding, errors, expected):
    # Check that the error handler is correctly registered.
    def handler(exception):
        return (expected, exception.end)
    codecs.register_error(errors, handler)
    # Check that the error handler is correctly returned.
    handler2 = codecs.lookup_error(errors)
    if handler2 is not handler:
        raise AssertionError("lookup_error() did not return the expected "
                             "error handler")
    # Check that the error handler is correctly used.
    decoder = codecs.getdecoder(encoding)
    result, consumed = decoder("\xff", errors)
    if result != expected or consumed != 1:
        raise AssertionError("getdecoder() did not use the expected "
                             "error handler")

def test_main():
    check_register_error("ascii", "strict", "")
    check_
