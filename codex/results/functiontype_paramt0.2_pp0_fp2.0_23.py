from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# list(map(lambda x: x, range(10)))

# list(filter(lambda x: x, range(10)))

# list(zip(range(10), range(10)))

# list(enumerate(range(10)))

# list(reversed(range(10)))

# list(sorted(range(10)))

# list(sorted(range(10), reverse=True))

# list(sorted(range(10), key=lambda x: -x))

# list(sorted(range(10), key=lambda x: x % 2))

# list(sorted(range(10), key=lambda x: x % 2, reverse=True))

# list(sorted(range(10), key=lambda x: x % 2, reverse=True))

# list(sorted(range(10), key=lambda x: x % 2, reverse=True))

# list(sorted(range(10), key=lambda x: x % 2, reverse=
