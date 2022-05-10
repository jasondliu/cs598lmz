from types import FunctionType
list(FunctionType(compile("", "", "exec"), {}, "") for i in range(2))

# PyPy doesn't support __sizeof__ yet
#assert list.__sizeof__() == 56

l = list(range(3))
