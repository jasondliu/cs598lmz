import codecs
# Test codecs.register_error('myerror', myerror)

# This is a simple example to show how to handle errors in codecs.
# The errorhandler function is called with an exception instance
# that describes the error.  The values of this exception are the
# following:
#
#     encoding: The name of the encoding that raised the error.
#     reason: A string describing the specific codec error.
#     start: The first position in the input string where the error
#            occurred.  This will be None if the codec can't determine
#            this information.
#     end: The position where the input string ends.  This will be None
#          if the codec can't determine this information.
#     object: The object which caused the error.  This will be None
#             if not available.
#
# The errorhandler function can return a (replacement, newposition)
# tuple.  The replacement is the replacement string for the input that
# caused the error.  The newposition is the position where parsing
# should continue (starting from the beginning of the string).
#
# If the errorhandler function raises a UnicodeError, the unenc
