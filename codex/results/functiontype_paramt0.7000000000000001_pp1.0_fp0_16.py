from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, argdefs=f.__defaults__,
                 closure=f.__closure__) for f in (f1, f2, f3))
# [<function f1 at 0x100dbc7d0>, <function f2 at 0x100dbc8c0>, <function f3 at 0x100dbc950>]

# In Python 2, this can be done with exec and eval, but Python 3's exec and eval
# do not work with functions. It is possible to hack it in Python 3 by using
# importlib, but the result is not a function.

import importlib
spec = importlib.util.spec_from_loader('', importlib.machinery.SourceFileLoader('', 'funcs.py'))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def make_function(code, globs=None, name=None, argdefs=None, closure=None):
    """Create a function object from a code object and optional globals.
