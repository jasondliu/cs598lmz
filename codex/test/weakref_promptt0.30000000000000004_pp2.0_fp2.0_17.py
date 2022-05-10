import weakref
# Test weakref.ref() with a class that has a __del__ method.
#
# This test is a bit tricky, because we need to make sure that the
# weak reference doesn't keep the object alive.  We do this by
# creating a cycle, and then deleting the cycle explicitly.
#
# The test is a bit tricky, because we need to make sure that the
# weak reference doesn't keep the object alive.  We do this by
# creating a cycle, and then deleting the cycle explicitly.

class C:
    def __init__(self, x):
        self.x = x
        self.y = weakref.ref(self)
