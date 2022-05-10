import weakref
# Test weakref.ref() with a callable object
#
# This is a test for SF bug #836347.

class Foo:
    def __call__(self):
        return 42

