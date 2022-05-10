from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(map(lambda x: x, range(10)))

# list(filter(lambda x: x, range(10)))

# list(zip(range(10), range(10)))

# list(enumerate(range(10)))

# list(reversed(range(10)))

# list(sorted(range(10)))

# list(range(10))

# list(range(10, 0, -1))

# list(range(10, 0, -2))

# list(range(10, 0, 2))

# list(range(10, 0, 1))

# list(range(10, 0, 0))

# list(range(10, 0, -0))

# list(range(10, 0, -1.0))

# list(range(10, 0, -0.0))

# list(range(10, 0, -1.1))

# list(range(10, 0, -1.1))

