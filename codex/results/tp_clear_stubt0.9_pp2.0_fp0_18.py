import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect()
print('ok')
'''
    def test_uncollectable_gc(self):
        import weakref, gc
        class A:
            pass
        a1 = A()
        a1.a2 = a2 = A()
        a2.a3 = a3 = A()
        a3.a1 = a1

        a1.__del__ = a2.__del__ = a3.__del__ = lambda: None # make objects un-collectable

        # trigger collection of a1 and a3
        x = weakref.ref(a1); x()
        x = weakref.ref(a3); x()
        gc.collect()

        # now we have all three objects as uncollectable non-reachable cycles
        # delete a2 to make the cycle unreachable
        del a1.a2
        del a2
        gc.collect()

        # now, a1 and a3 should be reachable again.
        assert not gc.garbage, gc.garbage

    def test_long__new
