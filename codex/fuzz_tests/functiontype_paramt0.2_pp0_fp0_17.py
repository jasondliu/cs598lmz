from types import FunctionType
list(FunctionType(lambda: None, globals()).__code__.co_consts)

# ['<code object <lambda> at 0x7f4f7e8e3c30, file "<stdin>", line 1>', None]

# The first item is the code object for the lambda function. The second item is the value None.

# The code object is a read-only object that contains information about the compiled code, including the bytecode instructions.

# The bytecode instructions are in a tuple called co_code.

# The names used in the bytecode instructions are found in co_names.

# The constants used in the bytecode instructions are found in co_consts.

# The variable names that are referenced in the bytecode instructions are found in co_varnames.

# The names of the global variables that are referenced in the bytecode instructions are found in co_names.

# The names of the built-in functions that are referenced in the bytecode instructions are found in co_names.

# The names of the free variables that are referenced in the bytecode instructions are found in co_cellvars.
