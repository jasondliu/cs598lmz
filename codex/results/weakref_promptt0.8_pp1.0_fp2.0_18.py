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
    print func.__name__, args, '=>', r
    try:
        rr = r()
    except TypeError, msg:
        print "calling a weak reference to a built-in type should return None"
    else:
        print 'built-in type dead reference should have raised TypeError'
        print 'Actual value returned:', rr

for T in [None, int, long, float, complex, str, unicode, tuple, list, dict, set, frozenset,
          file, C, D, weakref.ref]:
    _test
