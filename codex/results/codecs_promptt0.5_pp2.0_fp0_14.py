import codecs
# Test codecs.register_error()

# This test is for the codecs.register_error API.
#
# The API is used to register error handlers for codecs.
#
# The API is:
#   codecs.register_error(name, handler)
#
# The name is the name of the error handler, such as 'strict', 'replace',
# 'ignore', 'xmlcharrefreplace', 'backslashreplace'.
#
# The handler is a function which is called with:
#   exception instance
#   encoding
#   string
#   start position
#   end position
#   reason
#
# The handler should return a unicode string.
#
# The following tests are done:
#   1. register_error() with name 'test' is called with a handler.
#   2. The codec 'test' is used and the handler is called.
#   3. The handler is called with the correct arguments.
#   4. The handler returns a unicode string.
#   5. The returned unicode string is the expected value.
#   6. The codec 'test' is used and the handler is
