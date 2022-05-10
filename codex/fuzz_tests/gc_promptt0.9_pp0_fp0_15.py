import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before we create anything.
if verbose:
    print "calling gc.collect()"
gc.collect()
if verbose:
    raw_input("Hit any key to continue...")

gc.enable()

if verbose:
    print "creating objects"

# test weak callback registration and hash correctness
class WDict(dict):
    def __del__(self):
        if verbose:
            print "WDict.__del__()"

class ListOfWeakrefs(list):
    def __del__(self):
        if verbose:
            print "ListOfWeakrefs.__del__()"

class Callback:
    def __call__(self, *args, **kw):
        if verbose:
            print "Callback.__call__(...)"
    def __del__(self):
        if verbose:
            print "Callback.__del__(...)"

class A:
    def __del__(self):
        if verbose:
            print "A.__del__"

class NonCyclic:

