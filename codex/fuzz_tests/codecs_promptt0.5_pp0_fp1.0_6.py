import codecs
# Test codecs.register_error()

# This test script is a basic test of the codecs module.
# It is not intended to be a replacement for the extensive
# regression tests found in ../Lib/test/test_codecs.py

import sys
from test import test_support

def verify(encoding):
    print 'Testing encoding:', encoding

    # Encode some Unicode strings
    s1 = u'\u00e9\u00e9\u00e9'
    s2 = u'\u00e9'
    s3 = u'\u00e9\u00e9\u00e9\u00e9'
    s4 = u'\u00e9\u00e9\u00e9\u00e9\u00e9'
    s5 = u'\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9'
    s6 = u'\u00e9\u00e9\u00e9\u00e9\u00e9\u00
