fn = lambda: None
# Test fn.__code__
pyfunc_name_fn()
pyfunc_name_fn.__name__
pyfunc_name_fn.__code__.co_name
pyfunc_name_fn.__code__.co_filename
pyfunc_name_fn.__code__.co_firstlineno
pyfunc_name_fn.__code__.co_argcount
pyfunc_name_fn.__code__.co_varnames
pyfunc_name_fn.__code__.co_cellvars
pyfunc_name_fn.__code__.co_freevars

def pyfunc_name_fn_2():
    def pyfunc_name_fn_2_nested_1(a=1): pass
# Test fn.__code__ that has a nested function
pyfunc_name_fn_2()
pyfunc_name_fn_2.__name__
pyfunc_name_fn_2.__code__.co_name
pyfunc_name_fn_2.__code__.co_filename
pyfunc_name_fn_2.__code__.co_firstlin
