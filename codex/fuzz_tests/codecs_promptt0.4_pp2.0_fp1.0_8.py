import codecs
# Test codecs.register_error()
#
# Use the "namereplace" error handler to replace unencodable characters
# with their name.

import codecs
import string

# This error handler replaces unencodable characters with their name.
def namereplace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    s = [u'\\x%02x' % ord(c) for c in exc.object[exc.start:exc.end]]
    return (u' '.join(s), exc.end)

# Register the error handler under a name
codecs.register_error('test.namereplace', namereplace)

# Encode a string with the error handler
s = u'Andr\xe9'
encoded = s.encode('ascii', 'test.namereplace')
print encoded

# The error handler is now registered globally, and can be used by
# all codecs that use the 'replace' error handler.

# This will replace unencodable characters with their name
print s
