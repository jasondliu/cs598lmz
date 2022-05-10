from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda x: x')(x) for x in range(5))

# lambda x: x is a short version of
# def f(x):
#     return x
# f

# list comprehension is a short version of
# [f(x) for x in range(5)]

# list(f(x) for x in range(5))

# list(map(f, range(5)))
# list(map(lambda x: x, range(5)))

# list(filter(lambda x: x % 2 == 0, range(5)))
# list(filter(lambda x: x % 2, range(5)))

# list(map(int, '123'))
# list(map(str, range(5)))

# list(map(lambda x, y: x + y, range(5), range(5)))
# list(map(lambda x, y: x + y, 'abc', '123'))

# list(map(pow, range(5), range(5)))
# list(map(pow, range
