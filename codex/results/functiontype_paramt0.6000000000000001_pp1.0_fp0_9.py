from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# [Out]
# ['<lambda>']

# Or even better:
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# [Out]
# ['x']

# We are now able to create a function with a given name:
def make_function(name, code):
    return FunctionType(code, {}, name=name)

# And, as a bonus, we can now pass a code object as the first argument to eval().
eval(make_function('foo', compile('lambda: None', '', 'eval')), {})

# [Out]
# <function foo at 0x7f8b7e5e5488>

# We can also use this technique to create a function with a docstring:
def make_function(name, code, docstring):
    return FunctionType(code, {}, name=name, doc=docstring)

# Or a function with a custom globals:
def make_function(name, code, globals
