from types import FunctionType
list(FunctionType(lambda: 0, globals(), 'foo') for _ in range(10))

# Create a list of 10 functions with the same name
list(FunctionType(lambda: 0, globals(), 'foo') for _ in range(10))

# Create a list of 10 functions with different names
list(FunctionType(lambda: 0, globals(), 'foo{}'.format(i)) for i in range(10))

# Create a list of 10 functions with different names
list(FunctionType(lambda: 0, globals(), 'foo{}'.format(i)) for i in range(10))

# Create a list of 10 functions with different names
list(FunctionType(lambda: 0, globals(), 'foo{}'.format(i)) for i in range(10))

# Create a list of 10 functions with different names
list(FunctionType(lambda: 0, globals(), 'foo{}'.format(i)) for i in range(10))

# Create a list of 10 functions with different names
list(FunctionType(lambda: 0, globals(), 'foo{}'.format(i)) for i in range
