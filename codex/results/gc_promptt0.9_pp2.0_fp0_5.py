import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A: pass
a = A()
weakref.ref(a)
del a
refs = gc.collect()
if refs != 1: print refs,
# Test gc.get_stats()
refs = gc.get_stats()
if refs != (None, None, None): print refs,

# Test __del__
gc.collect()
class A: 
    def __del__(self):
        self.a

a = A()
a.a = a
#del a
gc.collect()
# Test weakref
def f():
    pass
#print weakref.proxy(f)

class A: pass
a=A()
weakref.ref(a)
del a
gc.collect()
del a
gc.collect()
