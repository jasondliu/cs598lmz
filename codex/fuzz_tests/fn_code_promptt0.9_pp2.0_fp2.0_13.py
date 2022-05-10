fn = lambda: None
# Test fn.__code__
code_name = code_fn1.__name__
code_argcount = code_fn1.__code__.co_argcount
code_kwonlyargcount = code_fn1.__code__.co_kwonlyargcount
code_nlocals = code_fn1.__code__.co_nlocals
code_stacksize = code_fn1.__code__.co_stacksize
code_flags = code_fn1.__code__.co_flags
code_firstlineno = code_fn1.__code__.co_firstlineno
code_filename = code_fn1.__code__.co_filename
code_mconsts = code_fn1.__code__.co_consts
code_names = code_fn1.__code__.co_names
code_varnames = code_fn1.__code__.co_varnames
code_freevars = code_fn1.__code__.co_freevars
code_cellvars = code_fn1.__code__.co_cellvars
# Test
