import codecs
# Test codecs.register_error
#
# codecs.register_error(code_name, handler)
# Register the error handler handler for encoding/decoding name. This can
# be used to add encoding error handlers, implemented in Python, to codecs.
# Alternatively, the name can be registered using the
# errors attribute of the codecs module.
#
# There are two standard handlers, 'strict' and 'ignore'.
#
# The registered handler will be called with an exception instance
# as argument. It should return a (replacement, new position) tuple.
#
# The replacement value can be either a Unicode string or a tuple.
# If it is a tuple, the values will be inserted into the result string
# by the encoder. This is useful for inserting special characters
# like the byte order mark into the result.
#
# The position is the start position of the faulty input in the
# input string, or the start position of the replacement in the
# result string.
#
# The handler can raise a different exception, which will be
# propagated to the caller as usual.

# change respect to 2.6: 
# input
