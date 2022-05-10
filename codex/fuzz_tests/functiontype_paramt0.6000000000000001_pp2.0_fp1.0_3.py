from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# [3]
# from types import FunctionType
# list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# [4]
# from types import FunctionType
# list(FunctionType(lambda x, y: x + y, {}).__code__.co_varnames)

# [5]
# from types import FunctionType
# list(FunctionType(lambda a, b, c, d, e: a * b * c * d * e, {}).__code__.co_varnames)

# [6]
# from types import FunctionType
# list(FunctionType(lambda x=1: x, {}).__code__.co_varnames)

# [7]
# from types import FunctionType
# list(FunctionType(lambda x=1, y=2: x + y, {}).__code__.co_varnames)

# [8]
# from types import FunctionType
# list(FunctionType(lambda *args:
