import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error_handler', my_error_handler)

def test_codecs_register_error(encoding):
    # Test codecs.register_error()
    #
    # This test is not exhaustive, but it tests the most common errors
    #
    # Note that the errors are tested in the reverse order of their
    # definition in the codecs module.  This is because the first
    # error handler that can handle the exception is used.
    #
    # The test is run for each encoding, so that the error handlers
    # can be tested for encodings that use replace, xmlcharrefreplace,
    # backslashreplace, or namereplace.
    #
    # The test is run for each error handler, so that the error
    # handlers can be tested for UnicodeEncodeError and
    # UnicodeDecodeError.
    #
    # The test is run for each error handler and each encoding,
