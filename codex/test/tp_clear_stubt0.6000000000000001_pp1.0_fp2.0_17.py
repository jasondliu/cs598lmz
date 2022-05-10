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

latefin.ref().__module__
""")

    def test_gc_in_del_method(self):
        self.assertCodeExecution("""
import gc

class Test:
    def __del__(self):
        print("del Test()")
        gc.collect()

t = Test()
del t
print("gc.collect()")
gc.collect()
print("done")
""")

    def test_gc_in_del_method_with_refs(self):
        self.assertCodeExecution("""
import gc

class Test:
    def __del__(self):
        print("del Test()")
        gc.collect()

t = Test()
del t
print("gc.collect()")
gc.collect()
print("done")
""")

    def test_gc_in_del_method_with_refs_2(self):
        self.assertCodeExecution("""
import gc

