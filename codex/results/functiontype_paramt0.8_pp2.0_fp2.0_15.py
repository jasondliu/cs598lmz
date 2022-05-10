from types import FunctionType
list(FunctionType(a, globals(), "Foo")())
