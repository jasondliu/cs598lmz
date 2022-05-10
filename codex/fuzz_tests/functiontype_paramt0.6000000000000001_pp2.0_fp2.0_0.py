from types import FunctionType
list(FunctionType(lambda x:x,globals(),'lambda').__globals__.keys())

# ['__loader__', '__name__', '__doc__', '__package__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']

# eval

# eval(expression, globals=None, locals=None)

# expression - a string representing a Python expression
# globals (optional) - a dictionary
# locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

eval('__import__("os").getcwd()')

# '/Users/jr/workspace/python101'

eval('__import__("os").getcwd()', {})

# '/Users/jr/workspace/python101'

eval('__import__("os").getcwd()', globals())

# '/Users/jr/workspace/python101'

eval('__import__("os").getcwd()', {"
