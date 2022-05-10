from types import FunctionType
list(FunctionType(sum.__code__, globals()))

sum(1, 2)

sum.__code__.co_varnames
sum.__code__.co_argcount
sum.__code__.co_filename
