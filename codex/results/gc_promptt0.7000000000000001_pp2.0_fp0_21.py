import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Test:
    pass

def f():
    pass

gc.collect()

t1 = Test()
t2 = Test()
t3 = Test()

t1.t2 = t2
t2.t3 = t3
t3.t1 = t1

del t1, t2, t3
gc.collect() # end of the list is only reachable via the cyclic garbage

a = Test()
b = Test()
a.a = a
b.a = a
a.b = b

del a, b
gc.collect() # end of the list is only reachable via the cyclic garbage

# Test weak reference callbacks
def callback(x, y):
    pass

a = Test()
b = Test()
a.a = a
b.a = a
a.b = b

wr1 = weakref.ref(a, callback)
wr2 = weakref.ref(b, callback)

del a, b
gc.collect() # end of the list is only reachable via the cyclic garbage


