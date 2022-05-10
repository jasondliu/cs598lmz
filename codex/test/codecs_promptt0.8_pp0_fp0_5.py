import codecs
# Test codecs.register_error()
#   http://docs.python.org/lib/codec-base-classes.html
#
#  Discussion
#    One of the great features of Python is its Unicode support,
#    allowing you to write multilanguage programs without understanding
#    all the details of character encodings.
#
#    Python supports three basic ways to handle errors that occur during
#    Unicode encoding or decoding:
#    Strict Error Handler
#       The default error handling mechanism in Python is called "strict".
#       If a decoding error occurs, it raises a UnicodeDecodeError.
#       If an encoding error occurs, it raises a UnicodeEncodeError.
#    Ignore Error Handler
#       You can force Python to ignore Unicode errors by using the
#       "ignore" error handler.
#    Replace Error Handler
#       Another error handling mechanism is the "replace" handler.
#       It will insert a special Unicode character, U+FFFD,
#       into the Unicode string that is returned.
#
#    The above error handlers are sufficient for most purposes.
#    However, it is possible to write a custom error handling function
