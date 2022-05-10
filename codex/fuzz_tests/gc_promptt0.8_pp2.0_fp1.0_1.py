import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect

class Foo:
    pass

class Bar:
    pass

f = []
f = [weakref.ref(Foo()),
     weakref.ref(Bar()),
     weakref.ref(Foo())]
for x in f:
    assert gc.collect() == 0
assert gc.collect() == 3

f = []
f = [weakref.ref(Foo()),
     weakref.ref(Bar()),
     weakref.ref(Foo())]
for x in f[:]:
    del x
assert gc.collect() == 3

# Check if gc.callbacks works

result = []
def callback(x):
    result.append(x)

class Foo():
    pass

w = [weakref.ref(Foo()),
     weakref.ref(Foo()),
     weakref.ref(Foo())]

gc.callbacks.append(callback)
gc.collect()
assert result == w

# Check if we invoke callbacks in the order they were added.
# (They
