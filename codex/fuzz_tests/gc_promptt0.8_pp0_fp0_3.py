import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
class Thing:

    def __del__(self):
        pass

    def __repr__(self):
        return 'Thing'

thing1 = Thing()
thing2 = Thing()

refs = [ weakref.ref(thing1), weakref.ref(thing2) ]
del thing1

gc.collect()

assert len(refs) == 2 and all(r() is not None for r in refs)

del thing2

gc.collect()

assert len(refs) == 2 and all(r() is not None for r in refs)

refs[0]().dummy = refs
refs[1]().dummy = refs
del thing1, thing2

gc.collect()

assert len(refs) == 2 and all(r() is not None for r in refs)

refs[0]()
refs[1]()
del thing1, thing2

gc.collect()

assert len(refs) == 2 and all(r() is not None for r in refs)

ref
