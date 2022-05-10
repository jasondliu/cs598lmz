import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
class D:
    pass
obj = D()
wr = weakref.ref(obj)
wrd = weakref.ref(D())
class C:
    pass
obj = C()
wr = weakref.ref(obj)
wrd = weakref.ref(C())
del obj
gc.collect()
gc.collect()
# Test gc.collect() with a subclass
class B:
    pass
class C(B):
    pass
obj = C()
wr = weakref.ref(obj)
wrd = weakref.ref(C())
del obj
gc.collect()
gc.collect()
# Test gc.collect() with a subclass of a builtin
class B(list):
    pass
class C(B):
    pass
obj = C()
wr = weakref.ref(obj)
wrd = weakref.ref(C())
del obj
gc.collect()
gc.collect()
# Test gc.collect() with a subclass of a builtin and a cycle
class B(list):
    pass
class C(B):
