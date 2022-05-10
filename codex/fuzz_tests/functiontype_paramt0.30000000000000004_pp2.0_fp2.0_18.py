from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# [<function <lambda> at 0x7f9e9a4b4c80>]

# This is a list of one element, which is a function object.
# The function object has a name, which is the string "lambda".
# The function object has a __globals__ attribute, which is a reference to the global namespace where it was defined.
# The function object has a __code__ attribute, which is a code object representing the compiled function body.

# The code object has a co_argcount attribute, which tells you how many arguments the function takes.
# The code object has a co_varnames attribute, which is a tuple containing the names of the local variables (including arguments).
# The code object has a co_names attribute, which is a tuple containing the names used by the bytecode.
# The code object has a co_consts attribute, which is a tuple containing the literals used by the bytecode.
# The code object has a co_code attribute, which is a string containing the raw bytecode.

# The bytecode is a sequence of
