from types import FunctionType
list(FunctionType(lambda x: (x, x), {"x": 1}))

# Not implemented
# list(map(lambda x: x + x, range(10)))
# list(map(None, range(10)))
# list(filter(lambda x: x & 1 and x > 3, range(10)))
# list(filter(None, range(10)))
# list(zip(range(10)))

# Tests for the map function
# list(map(lambda x: x + x, filter(lambda x: x & 1 and x > 3, range(10))))
# list(map(lambda x, y: x + y, filter(lambda x: x & 1 and x > 3, range(10)), range(10)))
# list(map(lambda x, y, z: x + y + z, filter(lambda x: x & 1 and x > 3, range(10)), range(10), range(20, 30)))
# list(map(lambda x, y=42: x + y, filter(lambda x: x & 1 and x > 3, range(10))))
# list(map(pow, (
