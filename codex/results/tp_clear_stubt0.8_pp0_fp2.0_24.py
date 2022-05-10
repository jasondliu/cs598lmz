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
func()
""")


def fin_del(obj):
    from rpython.rlib import rgc
    obj.__del__()
    rgc.collect()

def test_cycle_builtin_del():
    fin_del(CycleDelTest())

def test_simple_cycle_del():
    fin_del(SimpleCycleDelTest())

def test_too_late_finish():
    space = gettestobjspace(usemodules=['gc'])
    w_res = space.appexec([], """():
        def fin():
            fin.count = fin.count + 1
        fin.count = 0
        class A:
            pass
        A.fin = fin
        a = A()
        import sys, gc
        del A, fin
        gc.collect()
        # now it's too late to run the finish
        a.garbage = 42
        sys.getrefcount(a) - 1
        # but the finish should still be called
        return fin.count
    """)
   
