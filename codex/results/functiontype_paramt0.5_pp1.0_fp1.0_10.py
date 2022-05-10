from types import FunctionType
list(FunctionType(my_func.__code__, globals(), 'my_func'))

# Или вот так можно вызвать последний аргумент из кортежа в кортеже
def my_func(x, y, z):
    print(x, y, z)
my_func(*(1, 2, 3))

# Или вот так можно вызвать последний аргумент из кортежа в кортеже
def my_func(x, y, z):
    print(x, y, z)
my_func(*[1, 2, 3])

# Или вот так можн
