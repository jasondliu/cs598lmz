from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__).__closure__)

# []

def f(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def g(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def h(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def i(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def j(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def k(a, b=1, *, c, d=2, e=3, **kwargs):
    pass

def l(a, b=1, *, c, d=2, e=3
