gi = (i for i in ())
# Test gi.gi_code
gi.gi_code  # Should look like a function

# Test frame objects
def f(): pass
def g(x): return f
f.f_code
f.f_code.co_name == 'f'
f.f_code.co_name == 'g'  # g's code object, not f's
g(42).f_code == f.f_code  # g's code object, not f's

# Test stack frame objects
def h(x, y):
    a = x+y
    b = x-y
    c = a*b
    return c

import sys
sys.settrace(lambda *args: None)
try:
    h(1, 2)
except RuntimeError:
    pass
f = sys.exc_info()[2].tb_frame
# Test f.f_locals
f.f_locals  # Check that this works at all
f.f_locals == {'y': 2, 'x': 1, 'a': 3, 'b': -1, 'c': -3}

# Test
