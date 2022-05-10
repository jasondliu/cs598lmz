import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
a = weakref.ref(None)
gc.collect()
print a
gc.collect()
print a
gc.collect()
print a

# Test gc.get_objects()
a = weakref.ref(None)
for o in gc.get_objects():
    if isinstance(o, weakref.ref):
        if o() is None:
            print o

# Test gc.get_referrers()
a = weakref.ref(None)
for o in gc.get_referrers(a):
    if type(o) is dict:
        if '__weakref__' in o:
            print o

# Test gc.get_referents()
a = weakref.ref(None)
for o in gc.get_referents(a):
    if o is None:
        print o
