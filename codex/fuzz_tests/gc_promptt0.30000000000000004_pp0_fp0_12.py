import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class MyClass(object):
    pass

def f():
    x = MyClass()
    x.a = x
    wr = weakref.ref(x)
    del x
    gc.collect()
    return wr

wr = f()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
print wr()
