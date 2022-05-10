from types import FunctionType
list(FunctionType(f1.__code__,f1.__globals__,name=f1.__name__,argdefs=f1.__defaults__,closure=f1.__closure__))
