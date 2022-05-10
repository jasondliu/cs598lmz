import types
types.FunctionType(lambda: 0)

# CodeType is a built-in type for code objects.
# Code objects are used by the implementation to represent “pseudo-compiled” executable Python code such as a function body.
# They differ from function objects because they don’t contain a reference to their global execution environment.
# Code objects are returned by the built-in compile() function and can be extracted from function objects through their __code__ attribute.
# They are converted back into function objects by the built-in exec() and eval() functions.

# See also
# The documentation of the built-in compile() function.
# The documentation of the built-in exec() function.
# The documentation of the built-in eval() function.

# class code(argcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
# Create a code object.
# Not for the faint of heart.
# The details of the code object are described in Code Objects.
# The argcount, n
