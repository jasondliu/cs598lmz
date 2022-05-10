from types import FunctionType
list(FunctionType(lambda x: x+1, {})(1))

# This is a TypeError in Python 2.6.
# TypeError: 'function' object is not iterable
# list(lambda x: x+1)

# This is a TypeError in Python 2.6.
# TypeError: 'function' object is not iterable
# list(map(lambda x: x+1, []))

# This works in Python 2.6.
list(map(lambda x: x+1, {}))

# This is a TypeError in Python 2.6.
# TypeError: 'function' object is not iterable
# list(filter(lambda x: x+1, []))

# This is a TypeError in Python 2.6.
# TypeError: 'function' object is not iterable
# list(filter(lambda x: x+1, {}))

# This is a TypeError in Python 2.6.
# TypeError: 'function' object is not iterable
# list(reduce(lambda x: x+1, []))

# This is a TypeError in Python 2.
