from types import FunctionType
list(FunctionType(int, **globals())().__module__)
