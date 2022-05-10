import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect, gc.garbage, gc.get_referents, gc.get_referrers

class Foo:
    pass

class Bar:
    pass

class Spam(Foo, Bar):
    pass

class C:
    pass

def test(verbose=None):
    if verbose is None:
        verbose = gc.isenabled()
    # Create a cycle, and suppress the cyclic garbage collector
    s = Spam()
    s.x = s
    t = Spam()
    t.x = t
    t.y = t
    del t
    if verbose:
        print(gc.garbage)
    if gc.garbage:
        if verbose:
            print('no cycle', gc.get_referrers(Foo))
            print('with cycle', gc.get_referrers(s))
            print('just the class', gc.get_referrers(Foo.__class__))
            print('two classes', gc.get_referrers(Foo.__
