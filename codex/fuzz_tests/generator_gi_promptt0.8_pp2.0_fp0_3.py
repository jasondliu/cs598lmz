gi = (i for i in ())
# Test gi.gi_code is not NULL
next(gi)
def f(x, y=1): pass
f.__code__
def f(x, y=1): pass
# Test code.co_varnames is not NULL
f.__code__
def f(x, y=1): pass
# Test code.co_names is not NULL
f.__code__
def f(x, y=1): pass
# Test code.co_consts is not NULL
f.__code__
def f(x, y=1): pass
# Test code.co_cellvars is not NULL
f.__code__
def f(x, y=1): pass
# Test code.co_freevars is not NULL
f.__code__
import sys
# Test sys.flags is not NULL
sys.flags
import sys
# Test sys.float_repr_style is not NULL
sys.float_repr_style
import sys
# Test sys.path is not NULL
sys.path
import sys
# Test sys.warnoptions is not NULL
sys.warnoptions
import sys
# Test sys
