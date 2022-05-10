import codecs
# Test codecs.register_error

# This should raise a LookupError because 'decode_error' is not a valid
# error handler name.
