import codecs
# Test codecs.register_error()
test_support.import_module('locale')
test_support.import_module('sys')
startup_error = test_support.startup_error
try:
    test_support.import_module('unicodedata')
except ImportError:
    # skip this test...
    raise test_support.TestSkipped, 'unicodedata is not available on this platform'
import unittest
import random
import string

# Make sure sys.getfilesystemencoding() is available as
# sys.getfilesystemencoding used to be known as
# sys.getfilesystemencoding
try:
    sys.getfilesystemencoding()
except AttributeError:
    sys.getfilesystemencoding = lambda: sys.getfilesystemencode()

# This test is somewhat specific to the standard library.
def test_main():
    try:
        test_support.run_unittest(
            RegisterErrorTestCase, SearchFunctionTestCase,
            StreamReaderTestCase, StreamWriterTestCase,
            StreamRecoderTestCase, IncrementalEncoderTestCase,
            Incre
