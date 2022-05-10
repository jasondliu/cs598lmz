import codecs
# Test codecs.register_error()

# First, we'll test a basic error handler that simply substitutes '?'
# for the offending characters.

# The lookups will all be ASCII, so there's no need to do all that
# Unicode processing

# This is a class that can be used as an error handler.  The
# constructor is called with the exception that was raised, and the
# "methods" are called to handle various aspects of the error.
class my_error_handler:
    def __init__(self, exception):
        print('my_error_handler: got ', exception)
        self.exception = exception

    # This is called to handle the beginning of an encoding or decoding
    # operation.  This method should return the error handler object
    # to be used for the rest of the operation.
    # Note that this method is called from the constructor of the
    # IncrementalEncoder or IncrementalDecoder class, not from the
    # constructor of the error handler.  This means that this method
    # cannot use the self.exception attribute, because it doesn't exist
    # yet.
    def __call__(
