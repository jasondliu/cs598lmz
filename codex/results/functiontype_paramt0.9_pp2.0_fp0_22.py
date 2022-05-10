from types import FunctionType
list(FunctionType(lambda: make_gpib_wrapper(1), {}))
