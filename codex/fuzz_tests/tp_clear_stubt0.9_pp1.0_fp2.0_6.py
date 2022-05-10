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

def func():
    return 1

latefin.ref = weakref.ref(func)
del latefin
gc.collect()

func.__closure__
func.__closure__[0].cell_contents
''')

def _is_f():
    return f
f = 1
def f(): return 1
def f(x): return x

def test_builtin_code():
    assert code.co_name == "_f"
    assert eval(code) is _is_f

def test_mangling():
    eval('def p(__str__=1): pass')
    f = globals()['p']
    assert f.__name__ == 'p'
    assert f.__str__ == 1

    eval('def p(*__args__): pass')
    f = globals()['p']
    assert f.__name__ == 'p'
    assert f.__args__ == ()

    eval('def p(**__kwds__): pass')
    f = globals()['p']
    assert f.
