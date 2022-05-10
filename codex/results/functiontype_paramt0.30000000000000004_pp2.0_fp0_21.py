from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'addone')(i) for i in range(4))

# [1, 2, 3, 4]

# The first argument to FunctionType is the function body, which is a lambda expression in this case.
# The second argument is the global namespace.
# The third argument is the name of the function.

# The function is created and returned.
# We then pass it to list comprehension, and it is called for each value of i.

# The FunctionType constructor is rarely used directly.
# Instead, the built-in function eval is used to evaluate a string containing a Python expression.
# The resulting value is a function object.

addone = eval('lambda x: x+1')
addone
# <function <lambda> at 0x7f5c6a9f6e60>

addone(2)
# 3

# The eval function can also be used to evaluate a string containing a Python statement.
# The resulting value is None.

eval('print("Hello world!")')
# Hello world!

# eval can be used to evaluate
