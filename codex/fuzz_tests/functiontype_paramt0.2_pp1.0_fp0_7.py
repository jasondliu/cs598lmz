from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# TypeError: 'module' object is not iterable
# list(type(lambda x: x))

# TypeError: 'module' object is not iterable
# list(type(type(lambda x: x)))

# TypeError: 'module' object is not iterable
# list(type(type(type(lambda x: x))))

# TypeError: 'module' object is not iterable
# list(type(type(type(type(lambda x: x)))))

# TypeError: 'module' object is not iterable
# list(type(type(type(type(type(lambda x: x))))))

# TypeError: 'module' object is not iterable
# list(type(type(type(type(type(type(lambda x: x)))))))

# TypeError: 'module' object is not iterable
# list(type(type(type(type(type(type(type(lambda x: x))))))))

# TypeError: 'module' object is not iterable
# list(type(type(type(type
