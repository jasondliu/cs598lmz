from types import FunctionType
list(FunctionType(lambda x: print("hi"), globals(), "hi")())

# lambda with list comprehension
list(map(lambda x: x + 1, [1, 2, 3]))

# lambda with map function
list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))

# lambda with reduce function
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# lambda with filter function
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))

# lambda with a nested function
inner = lambda x: x * 2
outer = lambda x, y: inner(x) + y
outer(5, 6)

# lambda with a function parameter
def g(func, x, y):
    return func(x, y)
inner = lambda x, y: x * y
g(inner, 3, 4)
