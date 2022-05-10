from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
    argdefs=f.__defaults__, closure=f.__closure__) for f in (lambda: None,))

# Test __code__.co_flags
f = lambda: None
def f(): pass

list(f.__code__.co_flags & 0xFF for f in (f,))

# Test __code__.co_consts
list(f.__code__.co_consts for f in (f,))

# Test __code__.co_names
list(f.__code__.co_names for f in (f,))

# Test __code__.co_varnames
list(f.__code__.co_varnames for f in (f,))

# Test __code__.co_freevars
list(f.__code__.co_freevars for f in (f,))

# Test __code__.co_cellvars
