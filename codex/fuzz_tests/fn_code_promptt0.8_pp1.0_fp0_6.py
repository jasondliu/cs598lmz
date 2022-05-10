fn = lambda: None
# Test fn.__code__
codefn = fn.__code__
# Test codefn.__doc__
if codefn.__doc__ is not None:
    # Test codefn.__doc__.splitlines
    docs = codefn.__doc__.splitlines()
# Test codefn.co_argcount
# Test codefn.co_posonlyargcount
# Test codefn.co_kwonlyargcount
# Test codefn.co_nlocals
# Test codefn.co_stacksize
# Test codefn.co_flags
# Test codefn.co_firstlineno
# Test codefn.co_varnames
# Test codefn.co_names
# Test codefn.co_consts
# Test codefn.co_freevars
# Test codefn.co_cellvars
# Test codefn.co_filename
# Test codefn.co_name
# Test codefn.co_lnotab

with open(__file__, "rb") as f:
    file_data =
