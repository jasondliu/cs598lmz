import weakref
# Test weakref.ref(function)
#
# This tests that weak references to functions work correctly,
# and that the ref-counts of the functions' objects are correct.
#
# This also tests that weak references to instances, which are
# callable, work correctly.
#
# This test doesn't verify that the function objects can be
# deallocated, unless the function objects are module globals.
#
# XXXX It would be nice to test that the function objects can be
# XXXX deallocated, even if they aren't module globals.
#
# XXXX It would also be nice to verify that weak references to
# XXXX instance methods work correctly.
#
# XXXX We should test that the __call__ method works correctly as
# XXXX well -- that it works with classes that derive from 'object'.
#
import unittest


def function_global():
    pass


class C:

    def function_method0(self):
        pass

    def function_method1(self):
        pass

    def f(self):
        pass

    def __call__(self):
        pass


