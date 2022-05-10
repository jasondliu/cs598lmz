import codecs
# Test codecs.register_error

# The error handler must accept a UnicodeDecodeError as its first argument.
# The second argument is the encoding being used.

# If the error handler cannot handle the error, it must return a tuple
# (unicodeobject, int) or (str, int) where str is a string of length 1.

# The int is the number of characters consumed from the input.

# The error handler may return a tuple (None, int) to indicate that the
# error cannot be handled and the next error handler should be tried.

# If the error handler cannot handle the error, it must raise a TypeError.

# If the error handler has completely handled the error, it must return a
# unicode object.

# If the error handler has partially handled the error, it must return a
# tuple (unicodeobject, int) or (str, int) where str is a string of length 1.

# The int is the number of characters consumed from the input.

# If the error handler cannot handle the error, it must raise a TypeError.

# If the error handler has completely handled the error, it must return a

