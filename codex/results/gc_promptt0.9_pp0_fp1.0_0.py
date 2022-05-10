import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() really collects...

class obj(object):
    pass

def f(p):
    p.callback = weakref.ref(p)

def g(q):
    q.callback = weakref.ref(q)

a = obj()
b = obj()

a.callback = weakref.ref(b)
b.callback = weakref.ref(a)

a.x = obj()
b.x = obj()
a.x.callback = weakref.ref(b.x)
b.x.callback = weakref.ref(a.x)

f(a.x)
f(b.x)

a.x.x = obj()
b.x.x = obj()
g(a.x.x)
g(b.x.x)

del a
del b

found = gc.collect()
assert found == 11

assert obj.__del__.__dict__.get("func_code")
assert obj.__del__.im_func.__name__ == "__del__"
