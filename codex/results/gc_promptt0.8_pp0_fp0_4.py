import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class Foo(object):
    def __del__(self):
        print("del", self)
    def __repr__(self):
        return "<Foo with id %d>" % id(self)

f = Foo() # Prints 'del <Foo..>'
print("collecting")
gc.collect() # Prints 'del <Foo..>' again

# Test gc.garbage
f = Foo()
del f
print("collecting")
gc.collect() # Prints 'del <Foo..>' again
print("garbage is", gc.garbage) # Prints []
gc.garbage[:] = [f]
print("collecting")
gc.collect() # Prints 'del <Foo..>' again
print("garbage is", gc.garbage) # Prints [<Foo...>]

# Test weakrefs
class Foo(object):
    pass
a = Foo()
f = weakref.ref(a)
del a
del f
print("collecting")
gc.collect() # Prints nothing

