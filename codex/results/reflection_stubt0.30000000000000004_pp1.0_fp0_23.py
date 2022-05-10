fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__qualname__ = 'fn'

# A function with a closure
def fn2(x):
    y = x + 1
    def fn3(z):
        return x + y + z
    return fn3

# A function with a closure, but no free variables
def fn4(x):
    y = x + 1
    def fn5(z):
        return y + z
    return fn5

# A function with a closure, but no free variables
def fn6(x):
    y = x + 1
    def fn7(z):
        return y + z
    return fn7

# A function with a closure, but no free variables
def fn8(x):
    y = x + 1
    def fn9(z):
        return y
