import gc, weakref

def on_finalize(ref):
    print('on_finalize: object is going to be destroyed')

obj = SomeClass()
r = weakref.finalize(obj, on_finalize, obj)
r.alive
del obj
gc.collect()
r.alive

#The finalize callback is not invoked if the object is still alive after the
#garbage collection cycle.
o = SomeClass()
f = weakref.finalize(o, on_finalize, o)
f.alive
del o
f.alive

#finalize is a weak reference, so it can be discarded like any other weak
#reference, which will prevent its callback from ever being called.
o = SomeClass()
f = weakref.finalize(o, on_finalize, o)
f.alive
f.detach()
del o
f.alive

#Finalizing Objects That Participate in Reference Cycles

#The finalize callback is invoked even if the object is part of a reference
#cycle. As an example, consider this class that creates a cycle:

