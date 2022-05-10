import weakref
# Test weakref.ref built-in types
class C:
    def __init__(self, arg):
        self.value = arg

class D:
    def __init__(self, value=None):
        self.value = value
    def __cmp__(self, other):
        return cmp(self.value, other)
    def __repr__(self):
        return 'D(%r)' % self.value

from collections import deque
def _test(func, args):
    r = func(*args)
