from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), "square")(3))

# FunctionType(code, globals, name, argdefs, closure)
# code: code object
# globals: global namespace
# name: function name
# argdefs: default argument values
# closure: tuple of cell objects

# code object
# code object is a compiled function body.
# code object can be created by compile() function.

# compile() function
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# source: source code
# filename: file name
# mode: mode of compilation
# flags: compilation flags
# dont_inherit: if True, do not inherit flags from environment
# optimize: optimization level

# mode
# exec: compile source as a top-level statement
# eval: compile source as a single expression
# single: compile source as a single interactive statement

# flags
# PyCF_SOURCE_IS_UTF8: source is encoded in UTF-8
# PyCF_DONT_IMPLY_DEDENT: do
