import codecs
# Test codecs.register_error()

# This tests the codecs.register_error() function.

import codecs, encodings

# This is the error handler we want to register
def my_errorhandler(exception):
    # We will replace "a" with "b"
    return ("b", exception.start + 1)

# Register it
codecs.register_error("my_errorhandler", my_errorhandler)

# Encode a string with our registered error handler
encoded = "abc".encode("ascii", "my_errorhandler")

# Make sure it worked
