import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# index()
a = [1, 2, 3]
a.index(3)

# int()
a = '123'
int(a)

# isinstance()
class A:
    pass
a = A()
isinstance(a, A)

# issubclass()
class A:
    pass
class B(A):
    pass
issubclass(B, A)

# iter()
a = [1, 2, 3]
i = iter(a)
i.__next__()

# len()
a = [1, 2, 3]
len(a)

# list()
a = (1, 2, 3)
list(a)

# locals()
locals()

# map()
def square(x):
    return x ** 2

a = map(square, [1, 2, 3])
list(a)

# max()
a = [1, 2, 3]
max(a)

# memoryview()
a = memoryview(
