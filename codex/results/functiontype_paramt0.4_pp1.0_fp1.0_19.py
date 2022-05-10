from types import FunctionType
list(FunctionType(f, globals(), 'foo'))

# TypeError: 'foo' is not a Python function
#list(FunctionType(f, globals(), 'bar'))

# TypeError: argument must be code object
#list(FunctionType('hello, world'))

# TypeError: 'foo' is not a code object
#list(FunctionType(foo))

# TypeError: first argument must be code object
#list(FunctionType(f, None))

# TypeError: second argument must be a dictionary
#list(FunctionType(f, 'hello, world'))

# TypeError: third argument must be a string
#list(FunctionType(f, globals(), 1))

# TypeError: argument 3 must be string without null bytes
#list(FunctionType(f, globals(), 'foo\0bar'))

# TypeError: argument 3 must be string without null bytes
#list(FunctionType(f, globals(), 'foo\0bar'))

# TypeError: argument 3 must be string without null bytes
#list(FunctionType(f, globals(), 'foo
