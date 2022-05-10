import codecs
# Test codecs.register_error

# This test checks that codecs.register_error() works.

import codecs
import sys

# Error handler
def my_handler(exception):
    return ("test", exception.end)

# Register error handler
codecs.register_error("test.error", my_handler)

# Encode
