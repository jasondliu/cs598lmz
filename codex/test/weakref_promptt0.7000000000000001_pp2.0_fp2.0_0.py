import weakref
# Test weakref.ref(tuple())
t = tuple()
wr = weakref.ref(t)
del t
try:
    wr()
except:
    raise RuntimeError("weakref.ref(tuple()) failed")
# Test weakref.ref(tuple(...))
t = tuple([1, 2, 3])
wr = weakref.ref(t)
del t
try:
    wr()
except:
    raise RuntimeError("weakref.ref(tuple(...)) failed")
# Test weakref.ref(tuple(...)) where the tuple contains a weakref
t = tuple([1, 2, 3])
wr = weakref.ref(t)
t = tuple([1, wr, 3])
del wr
try:
    t[1]()
except:
    raise RuntimeError("weakref.ref(tuple(...)) failed")
# Test weakref.ref(tuple(...)) where the tuple contains a weakref which
# refers to itself
t = tuple([1, 2, 3])
wr = weakref.ref(t)
