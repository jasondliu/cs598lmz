from types import FunctionType
list(FunctionType(print, globals())(1,2,3))
