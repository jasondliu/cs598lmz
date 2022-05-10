import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
b = None
for i in range(8*2**14 / 4):
    a = [weakref.ref(x) for x in range(4)]
    del a
    b = [None] * 4
    del b

print gc.collect()
gc.collect()
print gc.garbage

# Test gc.set_debug(gc.DEBUG_LEAK)

import gc, weakref
gc.set_debug(gc.DEBUG_LEAK)
# Test gc.collect()
b = None
for i in range(8*2**14 / 4):
    a = [weakref.ref(x) for x in range(4)]
    del a
    b = [None] * 4
    del b

print gc.collect()
gc.collect()
print gc.garbage
