import weakref
# Test weakref.ref()

class Foo:
    pass

def callback(r):
    print("callback:", r)

f = Foo()
r = weakref.ref(f, callback)
print("r:", r)
print("f:", f)

f = None
print("deleted f")

import gc
gc.collect()
