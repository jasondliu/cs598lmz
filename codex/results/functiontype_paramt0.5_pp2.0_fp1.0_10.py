from types import FunctionType
list(FunctionType(lambda: None, globals()) for i in range(10))

# test_function_type_code
def f(): pass
f.__code__

# test_function_type_code_closure
def f(): pass
f.__code__.co_freevars

# test_function_type_code_defaults
def f(a, b=2, c=3): pass
f.__code__.co_varnames
f.__code__.co_argcount
f.__code__.co_kwonlyargcount
f.__code__.co_nlocals

# test_function_type_code_flags
def f(): pass
f.__code__.co_flags

# test_function_type_code_firstlineno
def f(): pass
f.__code__.co_firstlineno

# test_function_type_code_name
def f(): pass
f.__code__.co_name

# test_function_type_code_names
def f(): pass
f.__code__.co_names

#
