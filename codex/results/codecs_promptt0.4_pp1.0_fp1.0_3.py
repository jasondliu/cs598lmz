import codecs
# Test codecs.register_error()
import encodings

def test_main():
    # Test codecs.register_error()
    #
    # This test registers a custom error handler that simply
    # raises a UnicodeError with the input parameters.
    #
    # This is used to test the error handling in the various
    # codecs.
    #
    # The error handler is registered as 'strict' error handler
    # for all codecs.
    #
    # The test_codecmap_*() functions below are used to test the
    # error handler for the various codecs.
    #
    # Note that the error handler is registered with a custom
    # name, so that the standard codecs can still be used.
    #
    # The test_codecmap_*() functions are called with the custom
    # error handler name as parameter.
    #
    # The test_codecmap_*() functions use the 'strict' error handler
    # to test the error handler.
    #
    # The test_codecmap_*() functions are called with the custom
    # error handler name
