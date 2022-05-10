import codecs
# Test codecs.register_error

def test_register_error():
    # Test the codecs.register_error() API
    #
    # First, we need to create a codec that raises an error
    # when decoding.  We'll use the 'replace' error handler.
    #
    # The codecs module provides a helper function for this
    # purpose: codecs.lookup_error().  It takes the name of
    # an error handler and returns a tuple (function, name)
    # where 'function' is the error handler and 'name' is
    # the name of the error handler.
    #
    # The 'replace' error handler is a function that takes
    # a UnicodeDecodeError exception instance and returns
    # the replacement Unicode string.
    #
    # The 'replace' error handler is the default error
    # handler for most codecs.  It replaces malformed data
    # with the official Unicode replacement character,
    # U+FFFD.
    #
    # We can use the 'ignore' error handler as well.  It
    # simply discards the malformed data.
    #
   
