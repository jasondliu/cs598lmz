import codecs
# Test codecs.register_error()

# The codecs.register_error() function requires at least one argument,
# the name of an error handling function.  The function must take at
# least one argument, the exception instance, and can take up to three
# additional arguments.  The additional arguments are appended to the
# constructor of the exception, so you can use them to pass additional
# information to the error handler.

# Here's a simple example:
def my_errorhandler_1(exception):
    return ("some text", 1)

codecs.register_error("test.code.my_errorhandler_1", my_errorhandler_1)

# We're going to encode a string with the 'rot13' codec.  This codec
# encodes the latin alphabet with a ROT13 algorithm.  This is a
# simple scheme where each letter is replaced by the letter that is 13
# letters on.  The second argument to the error handler is a
# byte.  We're going to replace the byte 'a' with a byte that is
# 'a'+1.

# The string has two occurrences of the letter
