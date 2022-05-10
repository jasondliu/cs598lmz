import codecs
# Test codecs.register_error
from codecs import register_error

from test import support

import unittest
from test.support import import_module

def search_function(encoding):
    # NB (1).  This function must not raise LookupError for an unknown
    # encoding or unicode.  See bug 634676.
    # NB (2).  For the same reason, this function must not return None
    # for an unknown encoding.  See bug 872061.
    # NB (3).  For the same reason, this function must not return None
    # for an encoding for which it knows the codec, but that codec is
    # known to be broken.  See bug 1211549.
    if encoding == "test.unicode_internal":
        # The 'test.unicode_internal' codec should always be available,
        # see unicodeobject.c.
        from test import test_unicode_internal
        return (test_unicode_internal.encode,
                test_unicode_internal.decode,
                test_unicode_internal.incrementalencoder,
                test_unic
