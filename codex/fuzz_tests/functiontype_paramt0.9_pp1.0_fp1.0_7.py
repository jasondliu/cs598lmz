from types import FunctionType
list(FunctionType(x.__code__,x.__globals__,x.__name__,x.__defaults__,x.__closure__).__dict__)

# a list of one-parameter functions/objects implemented in C/Fortran/Cython will be found in globals()['__builtins__'] 
list(globals()['__builtins__'])

# only one-parameter functions will be returned
i=1; x=eval("print(i)"); list(x.__code__.co_names) # all the functions are assigned to a variable named 'x' in this case

i=1; y=abs; list(y.__code__.co_names)
i=1; y=bin; list(y.__code__.co_names)
i=1; y=cmp; list(y.__code__.co_names)
i=1; y=complex; list(y.__code__.co_names)
i=1; y=divmod; list(y.__code__.co_names)
i=1; y=
