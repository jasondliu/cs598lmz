from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure))

# or

def f():
    pass

from types import FunctionType
FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure)

# or

def f():
    pass

from types import FunctionType
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)

# or

def f():
    pass

from types import FunctionType
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)()

# or

def f():
    pass

from types import FunctionType
FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__
