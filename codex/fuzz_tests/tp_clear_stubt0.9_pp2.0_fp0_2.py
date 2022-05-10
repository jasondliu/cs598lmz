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
latefin.ref() is None and None
"""

class AppTestGarbageCollection(AppTestCpythonExtensionBase):
    spaceconfig = dict(usemodules=['_weakref'])

    def test_refcount_leak(self):
        module = self.import_extension('foo', [
            ("get_f", "METH_NOARGS",
             '''PyObject *obj = PyLong_FromLong(42);
                Py_INCREF(obj);
                Py_DECREF(obj);
                return obj;
             '''),
            ])
        module.get_f()
        del module.get_f

    def test_refcount_more(self):
        module = self.import_extension('foo', [
            ("get_f", "METH_O",
             '''PyObject *obj = PyLong_FromLong(42);
                Py_INCREF(obj);
                Py_DECREF(obj);
                return obj;
             '''),
            ])
        module.get_f(23)
