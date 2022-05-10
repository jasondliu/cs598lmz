import codecs
# Test codecs.register_error

# This test is not exhaustive.  It only tests the error handling
# mechanism, not the codecs themselves.

# The tests are designed to be run with the locale C so that we can
# test the fallback to the 'replace' handler.

import codecs, encodings.iso8859_1, encodings.iso8859_2
from test import test_support

# Error handlers

def strict_handler(exception):
    raise exception

def ignore_handler(exception):
    return (u"", exception.end)

def replace_handler(exception):
    return (u"?", exception.end)

def xmlcharrefreplace_handler(exception):
    return (u"&#%d;" % ord(exception.object[exception.start]), exception.end)

def backslashreplace_handler(exception):
    return (u"\\x%02x" % ord(exception.object[exception.start]), exception.end)

def namereplace_handler(exception):
    return (u"\\N{%s
