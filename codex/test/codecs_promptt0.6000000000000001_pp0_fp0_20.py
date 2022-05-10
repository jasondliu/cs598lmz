import codecs
# Test codecs.register_error
#
# This tests the ability to register error handlers with the codecs
# module. We'll test the behavior of the "xmlcharrefreplace" error
# handler.
#
# A few things to note:
#
# 1. The error handler must be registered with a name.
# 2. The name is used to look up the error handler when encoding
#    or decoding.
# 3. The error handler must be registered separately for encoding
#    and decoding.
# 4. The first argument to the error handler is the exception instance
#    that was raised.
# 5. The second argument to the error handler is the encoding of the
#    input or output.
# 6. The third argument to the error handler is the position in the
#    input or output string where the error occurred.
# 7. The fourth argument to the error handler is "True" if the
#    input or output is used for decoding, and "False" if it is
#    used for encoding.
# 8. The error handler must return a Unicode string.
#

#
# Register the error handler.
#
