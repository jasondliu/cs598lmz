from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# The __code__ attribute of a function is a read-only attribute that returns a
# code object representing the compiled function body. A code object has a
# co_varnames attribute that is a tuple containing the names of the local
# variables (including arguments).

# The code object returned by __code__ is the same object returned by the
# built-in function compile().

# The code object is a read-only object and cannot be modified.

# The code object returned by __code__ is not the same object as the func_code
# attribute of a function. The func_code attribute is the original code object
# as it was when the function was created. The __code__ attribute returns a
# modified code object with the compiler-related attributes removed.

# The __code__ attribute is not available for functions defined interactively
# or for functions compiled by the exec() function.

# The __code__ attribute is also not available for functions that are defined
# in C (built-in functions).

# The
