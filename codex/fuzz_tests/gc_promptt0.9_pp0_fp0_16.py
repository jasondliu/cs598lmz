import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect():
for _ in range(10):
    print()
    print('---', _)
    o1 = C(1)
    o2 = C(2)
    o2.other = o1
    o1.other = o2
del o1, o2
print(gc.collect())

gc.set_debug(0)
</code>
The output is:
<code>$ ./python -m test -v test_gc.py

...
test_gc.py::test_clear_types_with_weakrefs
set_debug(gc.DEBUG_COLLECTABLE)
--- 0
0
4
set_debug(gc.DEBUG_UNCOLLECTABLE)
--- 0
4
set_debug(gc.DEBUG_INSTANCES)
--- 0
4
set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
--- 0
8
set_debug(gc.DEBUG_INSTANCES | gc.DEBUG_UNCOLLECTABLE)
--- 0
8
set_debug(gc.DEBUG_COLLECTABLE | g
