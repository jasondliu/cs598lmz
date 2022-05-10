fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This test is not applicable for PyPy
# See http://bugs.pypy.org/issue1601
# fn.__code__ = 3
# raises(TypeError, fn)

# Test for issue #1629
def f():
    pass
f.__code__ = f.func_code
f()

def f():
    pass
f.__code__ = f.func_code
f.__defaults__ = (1,)
f()

def f():
    pass
f.__code__ = f.func_code
f.__closure__ = (1,)
f()

def f():
    pass
f.__code__ = f.func_code
f.__globals__ = {'1': 1}
f()

def f():
    pass
f.__code__ = f.func_code
f.__name__ = '1'
f()

def f():
    pass
f.__code__ = f.func_code
f.__doc__ = '1'
f()

def
