from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# TypeError: 'function' object is not iterable

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# TypeError: 'function' object is not iterable

# list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# TypeError
