fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

def f():
    yield 0

f.__code__ = None

# Exercise a codeless built-in function and a codeless type
__qt__ = type (f)
__qt__ (*(fn, fn))


# For optimization purposes, built-in functions have their func_code
# attributes hidden.  However, it should still be possible to
# modify, provided that the new value is set to None (thus making
# it really a Python function) and no code is executed afterwards.
# (This is all testing code paths in the PyEval_EvalFrameEx() C
# function.)
for func in (abs, delattr, hash, id, iter, len, min, max, round,
             setattr, sorted, sum, type, vars):
    assert func != getattr(func, 'func_code'), "func_code is not hidden"
    func.func_code = None
    assert func != getattr(func, 'func_code'), "func_code is not hidden"

# In rare cases, even built-in methods have their func_code
