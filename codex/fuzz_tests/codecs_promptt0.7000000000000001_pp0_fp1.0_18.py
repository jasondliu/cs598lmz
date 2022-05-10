import codecs
# Test codecs.register_error function
# We will define a special error handler that raises UnicodeDecodeError
# if a non-ASCII character is decoded.
#
# This error handler is useful in the context of an automated
# test suite, to detect the encoding of Python source files.

class NonAsciiError(UnicodeDecodeError):
    def __init__(self, msg, s, start, end, reason='<nothing>'):
        UnicodeDecodeError.__init__(self, msg, s, start, end)
        self.reason = reason
    def __str__(self):
        return UnicodeDecodeError.__str__(self) + ' (reason: %s)' % self.reason

def nonascii_error_handler(msg):
    def handler(s, start, end):
        reason = s[start:end]
        raise NonAsciiError(msg, s, start, end, reason)
    return handler

# The error handler must be registered at module level,
# so it can be passed as an argument to codecs.decode().
codecs.register
