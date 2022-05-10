from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(10))

# list(filter(None, [1, 0, 2, 0]))
# list(filter(lambda x: x, [1, 0, 2, 0]))

# list(map(lambda x: x, range(10)))
# list(map(lambda x: x**2, range(10)))
# list(map(lambda x, y: x+y, range(10), range(10)))

# list(filter(lambda x: x%2, range(10)))
# list(filter(lambda x: x%2==0, range(10)))

# list(map(lambda x: x**2, filter(lambda x: x%2, range(10))))

# list(map(lambda x: x**2, filter(lambda x: x%2==0, range(10))))

# list(filter(lambda x: x%2, map(lambda x: x**2, range(10))))

# list(filter(lambda x: x%2==0, map(lambda x:
