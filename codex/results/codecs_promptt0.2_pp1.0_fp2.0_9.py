import codecs
# Test codecs.register_error
#
# This test is not complete.  It is only a sanity check.

import codecs
import sys

def test(name, enc, errors):
    print 'Testing', name, 'with', errors
    s = u'\u3042\u3044\u3046'
    try:
        x = s.encode(enc, errors)
    except UnicodeError, detail:
        print 'UnicodeError:', detail
    else:
        print repr(x)
        print x.decode(enc, errors)

def test_register_error(name, enc, errors):
    print 'Testing', name, 'with', errors
    s = u'\u3042\u3044\u3046'
    try:
        x = s.encode(enc, errors)
    except UnicodeError, detail:
        print 'UnicodeError:', detail
    else:
        print repr(x)
        print x.decode(enc, errors)

def test_register_error_bad_handler(name, enc, errors):
    print '
