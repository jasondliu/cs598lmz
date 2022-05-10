fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14174: segfault when calling a function with a generator as
# __code__ and a __defaults__ containing a closure.
def f():
    def g():
        pass
    fn = lambda: None
    fn.__code__ = g
    fn.__defaults__ = (g,)
    fn()
f()

# Issue #14174: segfault when calling a function with a generator as
# __code__ and a __closure__.
def f():
    def g():
        pass
    fn = lambda: None
    fn.__code__ = g
    fn.__closure__ = (g,)
    fn()
f()

# Issue #14174: segfault when calling a function with a generator as
# __code__ and a __closure__ containing a closure.
def f():
    def g():
        pass
    fn = lambda: None
    fn.__code__ = g
    fn.__closure__ = (g,)
    fn()
f()

# Issue #14174: segf
