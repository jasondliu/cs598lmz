from types import FunctionType
list(FunctionType(add.func_code, globals(), 'add'))

def add(x, y):
    return x+y

add.__name__
add.__code__
add.__code__.co_name
add.__code__.co_varnames
add.__code__.co_argcount
add.__code__.co_flags
add.__code__.co_code
add.__code__.co_consts
add.__code__.co_names
add.__code__.co_nlocals
add.__code__.co_stacksize
add.__code__.co_filename
add.__code__.co_firstlineno
add.__code__.co_lnotab

def add(x, y, z):
    return x+y+z

add.__code__.co_argcount
add.__code__.co_varnames
add.__code__.co_argcount
add.__code__.co_nlocals
add.__code__.co_flags
add.__code__
