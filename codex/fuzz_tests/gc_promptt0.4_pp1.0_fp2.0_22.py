import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    x.b = x
    del x

f()
gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    x.b = x
    del x

f()
gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    x.b = x
    del x

f()
gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    x.b = x
    del x

f()
gc.collect()

class C:
    pass

def f():
    x = C()
    x.a = x
    x.b = x
    del x

f()
gc.collect()

class C:
    pass

def f():
    x = C()
    x.a
