from types import FunctionType
list(FunctionType(lambda: None).__globals__.items()) # list of global vars and functions for the function

# (__closure__, __dict__, __code__, __name__, __defaults__, __globals__, __kwdefaults__)
