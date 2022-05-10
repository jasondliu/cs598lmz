import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect completed
print(gc.collect())
# Iterate through all found objects
for obj in gc.get_objects():
    if isinstance(obj, weakref.ref):
        # Try to ref object
        print('Obj: %s Ref Object: %s' % (obj, obj()))
    else:
        # If not weakref, skip
        continue
# Show Garbage
print(gc.garbage)

## << EXERCISE >>
## Why the last output(gc.garbage) is None?
