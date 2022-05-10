from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "lambda")(1))

# tuple(None)
# TypeError: 'NoneType' object is not iterable

# tuple(1)
# TypeError: 'int' object is not iterable

# tuple(1.1)
# TypeError: 'float' object is not iterable

# tuple(True)
# TypeError: 'bool' object is not iterable

# tuple('')
# TypeError: 'str' object is not iterable

# tuple(b'')
# TypeError: 'bytes' object is not iterable

# tuple(bytearray())
# TypeError: 'bytearray' object is not iterable

# tuple(range(1))
# (0,)

# tuple(map(lambda x: x+1, [1]))
# (2,)

# tuple(filter(lambda x: x > 0, [1]))
# (1,)

# tuple(zip([1], [0]))
# ((1, 0),)

# tuple([1])

