from types import FunctionType
a = (x for x in [1])
@CallOnce
def f():
    pass

def g():
    pass

class A:
    def __init__(self, a):
        self.a = a

def test_dict_callonce(func):
    """Test a CallOnce wrapped function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@CallOnce
def h():
    pass

@CallOnce
def i(x):
    pass

def j(x):
    pass

def k(x, y):
    pass

def l(*args, **kwargs):
    pass

class B:
    def __init__(self, a):
        self.a = a
    def __call__(self, a):
        pass

@CallOnce
def m(x):
    pass

@CallOnce
def n(x):
    pass

class C:
    def __init__(self, a):
        self.a = a
    def __call__
