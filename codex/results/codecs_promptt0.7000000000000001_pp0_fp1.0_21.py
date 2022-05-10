import codecs
# Test codecs.register_error()
from sre_constants import error as RE_error
from sre_compile import compile as RE_compile

from test.test_support import verbose, run_unittest

if verbose:
    import sys
    import getopt
    def msg(label, s):
        try:
            print label, repr(s)
        except UnicodeEncodeError:
            print label, repr(s.encode("unicode-escape"))

# Test data

# Unicode string that can be encoded to latin-1
LATIN1_UNICODE = u"\xe9\u6c34\u0e9a\u3055\u0a71\u05d0\u20ac\u00e9"
# Latin-1 encoded version
LATIN1_STR = "\xe9\xa6\xb4\xca\xd9\x8a\xd5\x90\xe0\xa5\xb0\xe2\x82\xac\xe9"

# Unicode string that can be encoded to iso-8859-15

