import codecs
# Test codecs.register_error

# This tests that the codecs.register_error function works as documented.
# This function is used to register error handlers for the specified
# encoding.  The error handler must be a callable object that accepts
# a UnicodeEncodeError or UnicodeDecodeError exception instance as
# its first argument.  The error handler must return a (replacement,
# new position) tuple.  The replacement is a unicode object that will
# replace the unencodable or undecodable data.  The new position is an
# integer specifying the new position to continue encoding or decoding
# at.  If the new position is not given, it defaults to the old
# position, which usually means that the unencodable or undecodable
# data will be skipped.
#
# This test checks that the error handler is called, and that the
# replacement string is inserted into the output stream.  It does not
# check that the new position is honored.

import codecs

def handler(exception):
    return (u"<%s>" % exception.object[exception.start:exception.end],
            exception
