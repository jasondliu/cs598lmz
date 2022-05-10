from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(map(lambda x: x, range(10)))

# list(filter(lambda x: x, range(10)))

# list(map(lambda x: x, filter(lambda x: x, range(10))))

# list(filter(lambda x: x, map(lambda x: x, range(10))))

# list(map(lambda x: x, map(lambda x: x, range(10))))

# list(filter(lambda x: x, filter(lambda x: x, range(10))))

# list(map(lambda x: x, filter(lambda x: x, map(lambda x: x, range(10)))))

# list(filter(lambda x: x, map(lambda x: x, filter(lambda x: x, range(10)))))

# list(map(lambda x: x, map(lambda x: x, filter(lambda x: x, range(10)))))

# list(filter(lambda x: x, filter(lambda x: x, map(lambda x
