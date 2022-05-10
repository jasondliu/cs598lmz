import codecs
# Test codecs.register_error()
import codecs

def _hex(c):
    return c > 255 and "0x%x" % c or "%d" % c

def _test():
    import operator
    import functools
    import os
    import sys
    if not hasattr(sys, 'gettotalrefcount'):
        def gettotalrefcount():
            return 42
    else:
        gettotalrefcount = sys.gettotalrefcount
    verbose = 0
    if '-v' in sys.argv:
        verbose = 1

    def check(result, object="?"):
        if verbose:
            print(object, ":", result)
        if not result:
            print("Error in", object)
            if verbose:
                print(sys.exc_type, sys.exc_value)
            raise test_support.TestFailed

    def checkequal(result, expected, object="?"):
        if verbose:
            print(object, ":", result, "==", expected)
        if result != expected:
            print("Error in",
