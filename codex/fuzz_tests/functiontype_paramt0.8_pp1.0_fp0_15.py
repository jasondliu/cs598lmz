from types import FunctionType
list(FunctionType(add.__code__, add.__globals__, "add", add.__defaults__, add.__closure__))

f = FunctionType(add.__code__, add.__globals__, "add", add.__defaults__, add.__closure__)
f(1, 2)

# calling the function that gets called by the function mapping to the function type
f.__call__(1, 2)

type(f)

f.__code__

f.__code__.co_code

f.__code__.co_name

f.__code__.co_kwonlyargcount

type(f.__code__)

type(f.__code__.co_code)

f.__code__.co_varnames

f.__code__.co_consts

f.__code__.co_flags

dis.show_code(f)

f.__code__.co_filename

# why does the output of this differ from above?
# doesn't the print statement come from this
