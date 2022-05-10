import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
A = []
print(A)
print(gc.collect())
del A
gc.collect()
print(gc.collect())
A = []
A.append(A)
print(gc.collect())
# Test gc.garbage
class Foo:
    def __del__(self):
        gc.garbage.append(self)
gc.garbage[:] = []
obj = Foo()
del obj

print(gc.garbage)

gc.collect()

print(gc.garbage)

import os
pid = os.getpid()
print(gc.get_objects())
for obj in gc.get_objects():
    if isinstance(obj, list):
        print(obj)
        print(os.getpid())

import sys
sys.path.append('/usr/lib/python3.7/')
#sys.path.append('/usr/local/lib/python3.6/dist-packages/')
#sys.path.append('/usr/lib/python3.6/')

import pandas as pd
