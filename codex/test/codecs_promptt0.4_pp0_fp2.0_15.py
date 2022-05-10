import codecs
# Test codecs.register_error
# This is a test for the register_error function.
# The function is called with the following error handlers:
#
# - 'strict'
# - 'ignore'
# - 'replace'
# - 'xmlcharrefreplace'
# - 'backslashreplace'
#
# The function is also called with an error handler that raises
# a UnicodeError.
#
# The function is called with the following encoding:
#
# - 'ascii'
# - 'latin-1'
# - 'utf-8'
#
# The function is called with the following strings:
#
# - the empty string
# - a string that can be encoded with the given encoding
# - a string that can not be encoded with the given encoding
#
# The function is called with the following error handler:
#
# - a function that raises UnicodeError
# - a function that does not raise UnicodeError
#
# The function is also called with the following error handler:
#
# - a function that raises UnicodeError
# - a function that does not raise UnicodeError
#
# The function is also called
