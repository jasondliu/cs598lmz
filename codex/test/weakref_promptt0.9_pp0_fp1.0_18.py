import weakref
# Test weakref.ref()
r = weakref.ref(t)
r()

r() is None

import sys
sys.getrefcount(t)

r = weakref.ref(t)
sys.getrefcount(t)

sys.getrefcount(t) == 1

del t
