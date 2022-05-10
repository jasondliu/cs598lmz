import weakref
# Test weakref.ref() with objects of different types.


class C:
    pass


class D:
    pass


def callback(r):
    raise RuntimeError


objects = C(), D(), 'xyzzy', 10
for o in objects:
    ref = weakref.ref(o, callback)
    o2 = ref()
    del o
    gc.collect()
    if o2 is not None:
        print(o2)


# Test weakref.ref() with a class instance.
#
# This used to segfault if the class had a __cmp__ method.

import weakref


class C:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'C(%s)' % self.arg

    def __eq__(self, other):
        return self.arg == other.arg

    def __hash__(self):
        return hash(self.arg)


def callback(r):
    raise RuntimeError


c = C(10)
ref = weakref.ref(c,
