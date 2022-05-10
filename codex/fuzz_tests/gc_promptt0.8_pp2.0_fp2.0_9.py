import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() as a part of final functions.  It should
# only collect what it can, and not raise an error.

import copyreg

# A list of [before, after] pairs of uncollectable objects.  Refer to
# before objects as values in a dict (if we use them as keys, they get
# collected).
uncollectable = [
    [],
    [],
    ]

def reduce_ex(self):
    before = uncollectable[0].append(self)
    after = copyreg._reconstructor(self.__class__, ()).__reduce_ex__(2)
    return after

class C(object):
    def __reduce_ex__(self, proto):
        return reduce_ex, (self,)

c1 = C()
d = {c1: 1}
after = d[c1]

# Make c1 go away, but leave a reference to it in uncollectable[0].
c1 = None

# We don't want the above dict to keep d around, because we want to
# run gc.collect()
