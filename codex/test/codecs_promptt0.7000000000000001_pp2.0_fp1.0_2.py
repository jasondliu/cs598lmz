import codecs
# Test codecs.register_error to replace encoding error
# by Unicode U+fffd replacement character.
# See also <http://www.python.org/dev/peps/pep-0293/>.

import sys

def bad_encode(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.replace", bad_encode)

