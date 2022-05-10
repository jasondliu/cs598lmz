from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterable))
print(dir(a))

# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# [0,0,0,0,1,0,0,0,0]
