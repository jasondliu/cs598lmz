import codecs
# Test codecs.register_error
#
# This example is an extended version of the example given in
# the documentation for codecs.register_error()

# The most common errors are defined as exceptions
# in codecs.py

# Other errors are defined in the unicode module
# as attributes of the UnicodeError class

# Here we use the 'backslashreplace' error handler
# to replace characters that cannot be encoded with a
# backslash and the character's numeric value.

# First, we replace the standard 'strict' error handler
# with our own error handler function

def replace_error_handler(error):
    return (u'\\' + unicode(ord(error.object[error.start])) ,
            error.end)

codecs.register_error('replace', replace_error_handler)

# Now we encode a string with a character that cannot
# be encoded

s = u'pi: \u03c0'

# The default encoding is 'ascii' which cannot encode
# the character '\u03c0'

print s.encode('ascii')
