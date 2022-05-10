from types import FunctionType
list(FunctionType([], object()))
# 0
# >>> list(FunctionType([], [object(), object()]))
# 0
# >>> list(FunctionType([], (object(), object())))
# 0
# >>> list(FunctionType([], {object(), object()}))
# 0
# >>> list(FunctionType([], {object(): 1}))
# 1

# >>> list(FunctionType([], 123))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable

# >>> list(FunctionType([], '123'))
# ['1', '2', '3']

# >>> list(FunctionType([], False))
# [False]

# >>> list(FunctionType([], True))
# [True]

# >>> list(FunctionType([], None))
# [None]

# >>> list(FunctionType([], object()))
# []

# >>> list(FunctionType([], [object(), object()]))
# [<object object at 0x7f4379ce
