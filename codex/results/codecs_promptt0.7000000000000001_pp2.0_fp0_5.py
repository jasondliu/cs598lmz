import codecs
# Test codecs.register_error
#
# This test must be run with the -R switch, because it raises an exception
# whose identity it checks.  It also requires the old string module.

import sys
import string

def bad_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (exc.object[:exc.start] + "?" +
                exc.object[exc.end:], exc.end+1)
    elif isinstance(exc, UnicodeEncodeError):
        return (exc.object[:exc.start] + "?" +
                exc.object[exc.end:], exc.end+1)
    raise TypeError("don't know how to handle %r" % exc)

class MyError(UnicodeError):
    pass

def bad_replace2(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (exc.object[:exc.start] + "?" +
                exc.object[exc.end:], exc.end+1)
    elif isinstance(exc, UnicodeEncodeError):
        return (exc
