from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# [<function <lambda> at 0x7f0c7a7d5a60>, <function <lambda> at 0x7f0c7a7d5b90>]

# It is also possible to create a function from a string of Python code.
# This is called an evaluatable string.

from types import FunctionType
FunctionType(compile("x + 1", "<string>", "eval"), globals())

# <function <lambda> at 0x7f0c7a7d5c80>

# The first argument is the string of code, the second argument is the name of the file
# (or a description of the source), and the third argument is the mode of compilation.
# In this case, we are compiling an expression, so we use "eval".
# The last argument is the global namespace in which the function will be executed.
# This is used to resolve any global variables referenced in the code string.
# The function returned by compile() is a code object.
# The FunctionType() constructor takes a code object and returns a function.

