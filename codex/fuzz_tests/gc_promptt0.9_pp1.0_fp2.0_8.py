import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect_generations
gc.collect(0)
gc.collect(1)
gc.collect(2)
gc.collect(3)
gc.collect(4)
# Test if garbage collecting is enabled
print(gc.isenabled())
gc.disable()
gc.enable()

# Test garbage collector hooks
def f():
    print("i will be never executed")

def my_finalizer(o):
    print("my_finalizer is called")

l = []

print("building up cycle, just a little")
l.append(l)
l.append(l)
l.append(l)
l.append(l)
l.append(l)
l.append(l)
l.append(l)

def test_finalizers():
    print("running test_finalizer")
    o = object()
    o_wref = weakref.ref(o, f)
    print("triggering gc, this should execute finalizer")
    gc.collect()
    print("it is all")

def test_collect_generations():
    g
