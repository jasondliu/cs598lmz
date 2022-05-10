from types import FunctionType
list(FunctionType(lambda: 0, globals())())
