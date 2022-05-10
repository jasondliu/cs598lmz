from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'type' object is not iterable
# list(type(lambda x: x))

# TypeError: 'type' object is not iterable
# list(type(type(lambda x: x)))

# TypeError: 'type' object is not iterable
# list(type(type(type(lambda x: x))))

# TypeError: 'type' object is not iterable
# list(type(type(type(type(lambda x: x)))))

# TypeError: 'type' object is not iterable
# list(type(type(type(type(type(lambda x: x))))))

# TypeError: 'type' object is not iterable
# list(type(type(type(type(type(type(lambda x: x)))))))

# TypeError: 'type' object is not iterable
# list(type(type(type(type(type(type(type(lambda x: x))))))))

# TypeError: 'type' object is not iterable
# list(type(type(
