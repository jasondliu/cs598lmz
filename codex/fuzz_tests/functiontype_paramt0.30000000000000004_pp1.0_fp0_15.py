from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [lambda: None, lambda x: None, lambda x, y=42: None])

# Check that we can create a function with a closure, but no globals or defaults
def make_func():
    x = 42
    def f():
        return x
    return f
f = make_func()
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [f])

# Check that we can create a function with a closure containing a cell
def make_func():
    x = 42
    def f():
        return x
    return f
f = make_func()
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs
