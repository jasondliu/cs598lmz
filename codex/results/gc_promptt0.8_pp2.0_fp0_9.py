import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and weakref callback in the presence of cyclic
# garbage.  This test is not exhaustive.
class C(object):
    pass

class T:
    pass

D = {}
L = []
w = weakref.ref(D)

# Needs to be a function to hold a reference to the callback.
def kill(k, w=w):
    del D[k]
    print w, w()

print w(), w() is D

for k in range(20):
    x = C()
    D[k] = x

D[1] = x
D[2] = L
D[3] = L[:]
D[4] = T()

print
print w(), w() is D

weakref.ref(x, kill)
weakref.ref(L, kill)
weakref.ref(L, kill)
weakref.ref(L, kill)
weakref.ref(L, kill)

print
print w(), w() is D

# The following lines are tricky.  If weakref callbacks are run
# immediately
