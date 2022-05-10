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
latefin.ref()
"""

class AppRefCycle(object):
    def setup_class(cls):
        import gc
        cls.gc = gc

    def test_finalizer_for_app_ref_cycle_callable___module__(self):
        import gc
        self.gc.collect()
        from conftest import AppRefCycleModuleCallable

    def test_finalizer_for_app_ref_cycle_callable_im_class(self):
        import gc
        self.gc.collect()
        from conftest import AppRefCycleMethodCallable

    def test_finalizer_for_app_ref_cycle_callable_func_globals(self):
        import gc
        self.gc.collect()
        from conftest import AppRefCycleFunctionCallable

    def test_finalizer_for_app_ref_cycle_class(self):
        import gc
        self.gc.collect()
        from conftest import AppRefCycleClass

    def
