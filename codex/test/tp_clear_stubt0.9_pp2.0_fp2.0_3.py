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


def function_code_getter(func):
    global func1
    func1 = func
    func.__code__


def function_globals_getter(func):
    global func2
    func2 = func
    func.__globals__


def function_name_getter(func):
    global func3
    func3 = func
    func.__name__


def function_defaults_getter(func):
    global func4
    func4 = func
    func.__defaults__


def function_code_setter(func):
    global func5
    func5 = func
    func.__code__ = None

def function_globals_setter(func):
    global func6
    func6 = func
    func.__globals__ = None

def function_name_setter(func):
    global func7
    func7 = func
    func.__name__ = None


def function_defaults_setter(func):
    global func8
    func8 = func
