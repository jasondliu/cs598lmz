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
assert latefin.ref() is None
del latefin
gc.collect()
assert func() is None
"""

def test_del_module():
    """
    class C:
        x = 1
    c = C()
    mod = sys.modules.copy()
    mod['c'] = c
    del mod['c']
    c.x = 2
    """

def test_del_class():
    """
    class C:
        x = 1
    c = C()
    c.x = 2
    del C
    c.x = 3
    """

def test_del_class_subclass():
    """
    class C:
        x = 1
    class D(C):
        pass
    c = C()
    d = D()
    c.x = 2
    d.x = 3
    del C
    c.x = 4
    d.x = 5
    """

def test_del_class_subclass_subsubclass():
    """
    class C:
        x = 1
