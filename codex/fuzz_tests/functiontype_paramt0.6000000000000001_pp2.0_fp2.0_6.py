from types import FunctionType
list(FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__))

# out: [<function x at 0x7fba65b97e18>]

# list(FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__))
# out: [<function x at 0x7fba65b97e18>]

y = x()

list(FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__))

# out: [<function x at 0x7fba65b97e18>]

list(FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__))

# out: [<function x at 0x7fba65b97e18>]

y = x()

list(FunctionType
