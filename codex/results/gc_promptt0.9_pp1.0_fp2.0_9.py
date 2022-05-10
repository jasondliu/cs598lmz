import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() at an unexpected time.

# The details in this test are important.  In particular, running
# collect with 2 objects pending collection often crashes before the fix.  I
# don't know why.  Also, regrtest.py runs this file twice, with a gc.collect
# after the loop the first time, and at the end of the file the second time.
# That seems to work.

class C(object):
    pass

def f():
    ob = C()
    # create a cycle
    ob.attr = ob
    x = weakref.ref(ob)
    del ob
    assert gc.collect() == 1

for i in range(100):
    f()

l = []
for i in range(100):
    l += [C()]

del l
assert gc.collect() == 100

print "ok"
