from types import FunctionType
list(FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__).__code__.co_names)
</code>

