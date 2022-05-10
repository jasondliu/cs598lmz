fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'g'
fn(2, 3)


def f(x, y): return x + y
code = f.__code__
fn = types.FunctionType(code, globals())
fn(1, 2)
code = f.__code__.co_code
fn = types.FunctionType(code, globals(), f.__code__.co_name, f.__code__.co_defaults, f.__closure__)
fn(1, 2)
fn.__code__ = f.__code__
fn(1, 2)
code = f.__code__.co_code
fn = types.FunctionType(code, globals(), f.__code__.co_name, f.__code__.co_defaults, f.__closure__ if f.__closure__ else f.__closure__)
fn(1, 2)


def fn_with_closure():
    x = 1
    y = 2

    def g(x):
        return x + y
    return g


g = fn_
