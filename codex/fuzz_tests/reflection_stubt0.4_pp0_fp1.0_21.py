fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test __code__ and __closure__
def f():
    x = 1
    def g():
        return x
    return g

fn = f()
fn.__code__ = None
fn()

fn = f()
fn.__closure__ = None
fn()

# test __code__ and __defaults__
def f(a, b=1):
    return a, b

fn = f
fn.__code__ = None
fn(1)

fn = f
fn.__defaults__ = None
fn(1)

# test __code__ and __globals__
def f():
    return globals()

fn = f
fn.__code__ = None
fn()

fn = f
fn.__globals__ = None
fn()

# test __code__ and __kwdefaults__
def f(a, b=1, *, c=2, d=3):
    return a, b, c, d

fn = f
fn.__code__ = None
fn(1)
