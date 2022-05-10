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
latefin.ref = weakref.ref(func)
del latefin

gc.collect()
gc.collect()
gc.collect()
''')

def test_weakref_to_finalizer(space):
    gc.collect()
    # check that the "func" object is not alive
    assert space.is_true(space.w_None)
    func = space.appexec([], """():
        import gc
        l = gc.get_referrers(None)
        for obj in l:
            if not isinstance(obj, tuple):
                return obj
        return None
    """)
    assert func is not None
    # check that "func" is a valid function
    assert space.is_true(space.appexec([func], """(f):
        import gc
        try:
            f()
        except TypeError:
            return True
        else:
            return False
    """))

def test_weakref_to_finalizer_2(space):
    gc.collect()
    # check that the "
