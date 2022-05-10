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
del func, cyc, LateFin, Cyclic
gc.collect()

# we should have only one object
print(gc.collect())
print(len(gc.get_objects()))
print(dir(latefin))
latefin.__dict__['self'] = 'hello'
print(dir(latefin))
"""


# 'pickle' can modify __builtins__ without getting an EnvironmentError
def test_pickle_builtin_modification():
    # Issue #13305: pickle should not fail if __builtins__ is modified.
    data = pickle.dumps(int)
    mod = pickle.loads(data)
    __builtins__.mod = mod
    # pickle should use its own __builtins__, not the one passed by the user.
    # Thus, this should not change the original __builtins__.
    data = pickle.dumps(int, 2)
    del __builtins__.mod
    del mod
    # This should not crash.
    pickle.loads(data)


class C:
    class D:
        pass

class
