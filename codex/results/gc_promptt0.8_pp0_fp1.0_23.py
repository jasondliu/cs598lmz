import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, repr and weakref.
class Foo:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return "Foo(%r)" % self.arg

# Do it twice to also test cyclic trash with finalizers
for i in range(2):
    l = [Foo(i), Foo(i*10), Foo(i*100)]
    del l

# Collect and print all objects still alive.
gc.collect()
print(gc.garbage)


#weakref.finalize(o, lambda o=o: print('finalized', o))
#o = None
#print("End of program")
