from types import FunctionType
list(FunctionType(lambda x: x + x, globals(), '', (), None).__code__.co_varnames)

#   'x'

#   >>> from types import FunctionType
#   >>> list(FunctionType(lambda x: x + x, globals(), '', (), None).__code__.co_varnames)
#   ['x']
