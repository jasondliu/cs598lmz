gi = (i for i in ())
# Test gi.gi_code.co_stacksize for generators
def g():
    yield 1
    yield 2

g.gi_code.co_stacksize == 1
g.gi_code.co_stacksize == 1
# Test gi_frame.f_exc_traceback
def f():
    x = 1
    try:
        return x
    except (KeyError, AttributeError):
        pass
    finally:
        y = 2

f.gi_frame.f_exc_traceback is not None
# Test variable names
def f():
    x = 1
    y = 2

f.__code__.co_varnames == ('x', 'y')
# Test global/local
def f():
    global x
    x = 1
    y = 1

f.__code__.co_varnames == ('x', 'y')
f.__code__.co_varnames == ('x', 'y')
f.__code__.co_varnames == ('x', 'y')
# Test an exception traceback
import sys
def f():
