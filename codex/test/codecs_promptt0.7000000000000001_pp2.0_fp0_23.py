import codecs
# Test codecs.register_error('strict', codecs.strict_errors), see #4457
codecs.register_error('strict', codecs.strict_errors)

import doctest

# Check that the test harness works
def test_test_support():
    raise Exception("this test always fails")

# Utility functions

def findfile(file, here=__file__):
    import os.path
    from os import pardir
    path = os.path.join(os.path.dirname(os.path.abspath(here)), file)
    # In case we're running in the build directory
    if not os.path.exists(path):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(here))),
                            pardir, file)
    return path

# Basic test of sys.stdout and sys.stderr
def test_print():
    import sys
    print >>sys.stdout, "this is stdout"
