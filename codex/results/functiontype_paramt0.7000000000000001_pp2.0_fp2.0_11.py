from types import FunctionType
list(FunctionType(hello, globals(), "new_name"))
# new_name()

# lambda
# lambda x, y: x + y
# (lambda x, y: x + y)(1, 2)

# map
# map(lambda x: x + x, [1, 2, 3])
# list(map(lambda x: x + x, [1, 2, 3]))
# list(map(lambda x: x + x, (1, 2, 3)))
# list(map(lambda x, y: x + y, (1, 2, 3), (4, 5, 6)))

# filter
# list(filter(lambda x: x > 0, range(-5, 5)))

# reduce
# from functools import reduce
# reduce(lambda x, y: x + y, [1, 2, 3, 4])
# reduce(lambda x, y: x + y, [1, 2, 3, 4], -10)

# in operator
# 1 in [1, 2, 3]
# 1 not in [1, 2, 3]

# del operator
#
