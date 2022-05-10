import gc, weakref 
def test(u): 
    for i in xrange(1000000):
        a = gc.get_referrers(u) 
        assert len(a) == 1 
        a = gc.get_referrers(a) 
        assert len(a) == 1 

def test_no_weakref(u): 
    for i in xrange(1000000):
        a = gc.get_referrers(u) 
        assert len(a) == 1 
        a = gc.get_referrers(a) 
        assert len(a) == 1 

def test_weakref(u): 
    for i in xrange(1000000):
        a = gc.get_referrers(u) 
        assert len(a) == 1 
        a = weakref.getweakrefcount(a)
        assert a == 1 

import cProfile
u = range(10)
