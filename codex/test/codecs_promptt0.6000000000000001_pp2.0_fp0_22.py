import codecs
# Test codecs.register_error

# This test case is based on the example in the documentation
# for codecs.register_error
#
# XXX: The example uses "replace" instead of "ignore" as the
# error handler.  However, the example also encodes a non-ASCII
# character, which should raise a UnicodeEncodeError.  The
# "replace" error handler would replace the non-ASCII character
# with a question mark instead.

# The example's error handler replaces all non-ASCII characters
# with a question mark
def my_ignore_handler(exception):
    return (u'?', exception.end)
codecs.register_error("myignore", my_ignore_handler)

# Encode a Unicode string to ASCII using our custom error handler
encoded = u'a\xac\u1234\u20ac\u8000'.encode("ascii", "myignore")
print(encoded)
