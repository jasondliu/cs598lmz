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

class Sub(typing.Generic[T]):
    pass

class Sup(Sub[int]):
    __slots__ = ()

# The next line should, but doesn't call Sup.__del__()
del latefin

assert func is None"""


class BrokenProperty:
    __slots__ = ()


class BrokenClass:
    __slots__ = ()

    @property
    def x(self):
        raise BrokenProperty


code = f"""class BrokenClass:
    __slots__ = ()

    @property
    def x(self):
        raise BrokenProperty


class BrokenProperty:
    __slots__ = ()


def f():
    g()


def g():
    BrokenProperty()


f()"""

# Test attribute access on classes that invoke the metaclass
# metamethod __getattribute__(), which is usually invoked when
# accessing attributes on objects.
# See https://github.com/python/cpython/pull/19355 for context.
code = """class Metaclass(type):

