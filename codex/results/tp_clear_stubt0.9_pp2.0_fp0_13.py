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

ref = weakref.ref(latefin)
latefin = None
del LateFin

gc.collect()
gc.collect()
gc.collect()

assert not ref()  # the __del__ cyclic reference chain

# With a __dict__ inheriting from itself

class Base:
    pass

class A(Base):
    __slots__ = ()
    def __del__(self):
        self.__dict__ = self
        self.x = 3  # formerly crashed with KeyError


a = A()

# With a __weakref__ inheriting from itself

class TD:
    pass

class AD(TD):
    def __del__(self):
        self.__weakref__ = self
        self.x = 3  # formerly crashed with KeyError


a = AD()

# With a __dict__ of self

class AD2(TD):
    def __del__(self):
        self.__dict__ = self
        self.x = 3  # formerly crashed with KeyError

a = AD2()

# With
