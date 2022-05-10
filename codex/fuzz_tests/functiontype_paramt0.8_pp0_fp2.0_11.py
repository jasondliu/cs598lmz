from types import FunctionType
list(FunctionType("a","b","c").__code__.co_varnames)

FunctionType("a", "b", "c").__code__
FunctionType("a", "b", "c").__code__.co_varnames 
FunctionType("a", "b", "c").__code__.co_varnames[2]
FunctionType("a", "b", "c").__code__.co_varnames[1]
FunctionType("a", "b", "c").__code__.co_varnames[0]
