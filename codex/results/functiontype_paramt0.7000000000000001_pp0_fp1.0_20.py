from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__) for f in [f])

f

f

#f = lambda x:x

#list(f(x) for x in [f])

#f = lambda x:x

#f(f)

def f(x):
    return x

f(f)

f = lambda: lambda: lambda: lambda x:x

f()()()(f)

[f, f]

f

f()

f()()

f()()()

f()()()(f)
