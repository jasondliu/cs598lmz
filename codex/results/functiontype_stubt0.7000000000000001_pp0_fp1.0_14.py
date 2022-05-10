from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
a()

# print(isinstance(a, FunctionType))
# print(isinstance(b, FunctionType))
# print(isinstance(c, FunctionType))
