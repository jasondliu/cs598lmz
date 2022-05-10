import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

gc.collect()
print(len(gc.garbage))        # 0

for x in (B(), B(), B()):     # create a few instances
    x = x     # stop x being deallocated
del x         # remove the last reference to x
gc.collect()
print(len(gc.garbage))        # only 1

print(gc.garbage[0].__class__)   # <class '__main__.B'>

# Test a weakref

x = B()
weakref_x = weakref.ref(x)
print(weakref_x)   # <weakref at 0x7f8ad0dcc9e8; to 'B' at 0x7f8ad0dccf28>
print(x)           # <__main__.B object at 0x7f8ad0dccf28>
del x

if weakref_x() is not None:
    print("ERROR: weakref_x() is not None")
gc.collect()
print(len(gc.garbage))        # 0
