import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() versus gc.garbage:
def CreateObjects():
    oblist = []
    for i in range(500):
        oblist.append(gc.collectable())
    for ob in oblist[100:150]:
       del ob
    return oblist
ob1 = CreateObjects()
ob2 = CreateObjects()
del ob1
del ob2
gc.collect()
assert len(gc.garbage) == 600
gc.collect()
assert len(gc.garbage) == 0
gc.garbage.extend([gc.collectable(), gc.collectable(), gc.collectable()])
g1 = gc.garbage
g1 = g1[:]
del g1
print gc.garbage # doesn't contain the 4 objects in g1
# Test non-existing objects in gc.garbage:
gc.garbage.append(gc.collectable())
gc.garbage.append(gc.collectable())
gc.garbage.append(gc.collectable())
gc.garbage.append(42)
gc.garbage.append(gc
