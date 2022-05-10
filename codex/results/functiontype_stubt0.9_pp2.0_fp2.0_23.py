from types import FunctionType
a = (x for x in [1])

ufunc.types.append((type(a), FunctionType))

print(uarray(a, dtype=float))

a = (x for x in [1,2])
print(uarray(a, dtype=float))
