gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test frame.f_builtins
import sys
def f():
    pass
f.__code__.co_filename = '<string>'
sys._getframe().f_builtins

# Test frame.f_code.co_cellvars and co_freevars
def f():
    x = 1
    def g():
        return x
    g()
f.__code__.co_filename = '<string>'
sys._getframe(0).f_code.co_cellvars

# Test frame.f_code.co_filename
def f():
    pass
f.__code__.co_filename

# Test frame.f_code.co_firstlineno
def f():
    pass
f.__code__.co_firstlineno

# Test frame.f_code.co_flags
def f():
    pass
f.__code__.co_flags

# Test frame.f_code.co_lnotab
def f():
    pass
f.__code__.co_lnot
