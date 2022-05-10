from types import FunctionType
list(FunctionType(r,globals(),'x') for r in range(4))

# ReSharper restore InconsistentNaming
