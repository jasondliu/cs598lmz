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

# issue 115: make sure that the __module__ of a function cannot be set
# to None
f = lambda: None
try:
    f.__module__ = None
except TypeError:
    raise TestFailed("__module__ cannot be None")

# issue 229: make sure that the __module__ of a function is writable
# even when the function is created by a built-in
import marshal
def f(): pass
code = marshal.loads(marshal.dumps(f.__code__))
f = FunctionType(code, f.__globals__)
f.__module__ = "foo"
if f.__module__ != "foo":
    raise TestFailed("__module__ is not writable")

# Ensure that we can create a code object with no free variables and
# that the freevars attribute is writable
def f(): pass
code = marshal.loads(marshal.dumps(f.__code__))
FunctionType(code, {}).__code__.co_freevars = ('a',)
