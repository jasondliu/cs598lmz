import types
types.CodeType(0, 0, 0, 0, 0, "<code object <module> at 0x10e3a3f20, file '<ipython-input-1-d6e68db6f96f>', line 1>", ('',), (), ('my_x', 'my_y'), ('',), '', '', 0, b'')

# 'co_code' is a bytestring representing the compiled code

# 'co_nlocals' is the number of local variables (including arguments)

# 'co_varnames' is the tuple of names of local variables

# 'co_names' is the tuple of names used by the bytecode

# 'co_consts' is a tuple of constants used by the bytecode

# 'co_flags' is an integer encoding a set of flags that provide information about the code

# 'co_filename' is the filename from which this code was compiled

# 'co_name' is the name of the function/method/class

inspect.getargspec(func) # deprecated, use inspect.signature

inspect.sign
