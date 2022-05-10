import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
l = []
for i in range(10):
    l.append(Wrapper())

for obj in l:
    #    import pdb; pdb.set_trace()
    id_ref = obj.__del__()
    # Make sure it's invalidated
    assert id_ref() is None

for obj in l:
    # Make sure it doesn't point to anything valid
    assert obj.__del__() is None

del l
for i in range(100):
    gc.collect()

# Test del obj
l = []
for i in range(10):
    l.append(Wrapper())

for obj in l:
    del obj

for obj in l:
    # Make sure it doesn't point to anything valid
    assert obj.__del__() is None

# Regressions

class Foo(object):
    pass

class Bar(object):
    pass

def setup():
    print
    print 'gc.set_debug(gc.DEBUG_LEAK)'
    gc.set_debug(gc.DEBUG_
