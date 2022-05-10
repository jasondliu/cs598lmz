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
raise SystemExit

""")

    def test_finalize_new_class(self):
        self.expected_traceback = 0
        self.process('import test_new_class')
        gc.collect()

    def test_finalize_new_instancemethod(self):
        self.expected_traceback = 0
        self.process('import test_new_instancemethod')
        gc.collect()

    def test_finalize_new_method(self):
        self.expected_traceback = 0
        self.process('import test_new_method')
        gc.collect()

    def test_finalize_new_slots(self):
        self.expected_traceback = 0
        self.process('import test_new_slots')
        gc.collect()

    def test_finalize_new_super(self):
        self.expected_traceback = 0
        self.process('import test_new_super')
        gc.collect()

    def test_finalize_new_weakref(self):
        self.expected_trace
