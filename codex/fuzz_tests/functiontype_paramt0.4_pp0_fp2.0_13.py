from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: None, lambda x=None: None))
# [<function <lambda> at 0x7f0d6a4b6ea0>, <function <lambda> at 0x7f0d6a4b6f28>]

# FunctionType(code, globals, name, argdefs, closure)
#
# code: the code object representing the compiled function body
# globals: a dictionary representing the global namespace in which the function should be executed
# name: the name of the function
# argdefs: a tuple of default argument values
# closure: a tuple of cells that contain bindings for free variables

# __code__, __globals__, __name__, __defaults__, __closure__
#
# __code__: the code object representing the compiled function body
# __globals__: a dictionary representing the global namespace in which the function should be executed
# __name
