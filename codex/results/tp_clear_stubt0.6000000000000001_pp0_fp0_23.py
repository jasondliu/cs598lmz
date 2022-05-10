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
del func, cyc, LateFin, Cyclic
gc.collect()

repr(latefin)
"""

    def test_double_free_with_finalizer(self):
        from rpython.rlib import rgc
        from rpython.rlib.objectmodel import invoke_around_extcall
        from rpython.rlib import objectmodel

        def get_this():
            return objectmodel.instantiate(This)

        def get_that():
            return objectmodel.instantiate(That)

        class This:
            def __init__(self):
                self.x = 1
            def __del__(self):
                rgc.collect()

        class That:
            def __del__(self):
                rgc.collect()
                assert get_this().x == 1

        self.run_source(self.source_double_free_with_finalizer,
                        [get_this, get_that],
                        __name__)

    def test_double_free_with_finalizer_and_cyclic_finalizer(self):
        from rpython.rlib import
