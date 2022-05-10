import codecs
# Test codecs.register_error
# This tests that we can register an error handler with the codecs module
# This handler will be called by the codecs module when an error occurs.
# The codecs module will then re-raise the exception using the codec_error_registry
# dictionary to raise the appropriate exception for the type of error.
# This is a lot like the error handler that the codecs module has, but a custom one
# allows for more control on the type of exception that is raised.

# This is tested in the unicode_internal.py test.

# codec_error_registry

# Check that we can override the error handler for a codec
def handler_func(exception):
    raise RuntimeError("Caught exception in handler")

# Register new error handling function
