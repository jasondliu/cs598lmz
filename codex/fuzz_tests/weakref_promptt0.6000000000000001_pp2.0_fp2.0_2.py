import weakref
# Test weakref.ref() with a cyclic data structure.
import gc


class C:

    def __init__(self):
        self.contents = [self]


c = C()
r = weakref.ref(c)
c.contents = []
del c
gc.collect()
print(r() is None)
