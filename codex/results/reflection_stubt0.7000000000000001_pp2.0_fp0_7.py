fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

class MyException(Exception):
    pass

def raiser0():
    raise MyException
def raiser1(x):
    raise MyException
def raiser2(x, y):
    raise MyException
def raiser3(x, y, z):
    raise MyException

def returns_something():
    return 42

class C1:
    def f(self):
        pass

class C2(C1):
    def g(self):
        pass

class C3(C2):
    pass

class C4(C2):
    def f(self):
        pass

class C5(C4):
    pass

def f(x, y=fn, *args, **kwds):
    pass

class myclass:
    def __init__(self):
        self.x = 1

def f():
    return myclass()

class C6(C3):
    def f(self):
        pass

def f():
    def g():
        return myclass()
    return g()


