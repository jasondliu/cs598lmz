import weakref
# Test weakref.ref()'s ability to handle a cyclic reference.
import re
import sys

from test import support
from test.support import gc_collect


class C:
    pass

c = C()

r = weakref.ref(c)

c.x = r
del c
gc_collect()
assert re.match('^<weakref at [0-9a-f]+; to ', str(r))
assert r() is None


# Test weakref.ref()'s ability to handle a cyclic reference
# where the referent is the weakref itself.

class D:
    pass

d = D()
d.x = d

r = weakref.ref(d)

del d
gc_collect()
assert re.match('^<weakref at [0-9a-f]+; to ', str(r))
assert r() is None


class OldStyle:
    pass

o = OldStyle()

r = weakref.ref(o)

o.x = r
del o
gc_collect()
