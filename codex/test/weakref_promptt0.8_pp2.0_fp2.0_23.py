import weakref
# Test weakref.ref(list) and weakref.proxy(list)

import weakref

class C:
    pass

data = weakref.ref(C.__class__)
assert data() is C.__class__
data = weakref.proxy(C.__class__)
assert data is C.__class__
