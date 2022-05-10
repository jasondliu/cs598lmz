import codecs
# Test codecs.register_error with a UnicodeDecodeError

import codecs

# The error handler is called with the exception instance and the
# start and end index of the unencodable region.
def handler(exception):
    return ("<%d>" % ord(exception.object[exception.start]), exception.end)

codecs.register_error("test.myhandler", handler)

# Now, test the error handler
s = "\x80spam"
