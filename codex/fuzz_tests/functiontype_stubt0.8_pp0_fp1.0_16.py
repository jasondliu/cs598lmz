from types import FunctionType
a = (x for x in [1])
b = FunctionType({}, {})
for x in [a, b]:
    print(type(x))
    print(isinstance(x, tuple))
    print(isinstance(x, FunctionType))
