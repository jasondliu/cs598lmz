import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
assert not gc.collectable(object())
assert not gc.collectable(object())
assert tuple(gc.get_objects()) == ()

import string, sys
for c in string.ascii_letters:
    print(c, end='')
    sys.stdout.flush()
    a = object()
    assert gc.collectable(a)
    assert a in gc.get_objects()
    del a
    gc.collect()
    assert not gc.collectable(a)
    assert a not in gc.get_objects()
    gc.collect()
    assert not gc.collectable(a)
    assert a not in gc.get_objects()
print()
gc.collect()
# Test gc.get_referrers()

import weakref

x = []
y = [x]
z = [y]
w = [z]

# Get referrers of the list referred to by x.  There should be two:
# y and z.
r = gc.get_referrers
