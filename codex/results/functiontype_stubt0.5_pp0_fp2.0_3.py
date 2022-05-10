from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)
print(isinstance(a, FunctionType))

# range
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(range(1, 10))
print(list(range(1, 10)))
print(range(10))
print(list(range(10)))

# 
print(list(range(10, 1, -1)))
print(list(range(10, 0, -1)))
print(list(range(10, -1, -1)))
