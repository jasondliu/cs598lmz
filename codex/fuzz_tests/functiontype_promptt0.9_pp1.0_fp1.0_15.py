import types
# Test types.FunctionType (i.e., use f.func_code)

def wrap(f):
    def do(*args):
        return 2*f(*args)
    code = getattr(f, "func_code", f.__code__)
    return types.FunctionType(code, globals(), "wrapped",
                              f.__defaults__, f.__closure__)

def f(y):
    return y+5
wrapped_f = wrap(f)
assert f(5) == 10
assert wrapped_f(5) == 20

def g(y, z=6):
    return y+z
wrapped_g = wrap(g)
assert g(5) == 11
assert wrapped_g(5) == 17

def h(y, z=6):
    return 2*y+z
def i(y):
    return h(y, z=10)
wrapped_i = wrap(i)
assert i(5) == 20
assert wrapped_i(5) == 40

assert f.__defaults__ == (None,)
assert g.
