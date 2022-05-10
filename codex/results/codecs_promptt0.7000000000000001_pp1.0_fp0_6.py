import codecs
# Test codecs.register_error for non-codec error handlers

import codecs, sys

# An error handler that checks that the arguments it gets are the
# ones it expects to get.
def handler(exception):
    assert(exception.end == 1)
    assert(exception.start == 0)
    assert(exception.object == b'\x00\x00\x00')
    return (ord(b'?'), exception.end)

# Register the error handler
codecs.register_error("test.checkargs", handler)

# Try encoding a character with the codec, which will cause the
# error handler to be called
codecs.utf_32_encode("\u0000", "test.checkargs")

print("success")
