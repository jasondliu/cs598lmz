import ctypes
ctypes.cast(1, ctypes.py_object)

# Set
# setattr(obj, 'x', value) is equivalent to ``obj.x = value''

# Time
# time()
# sleep(secs)
# monotonic()
# perf_counter()
# process_time()

# Class Methods
# classmethod(function)
# staticmethod(function)

# Code
# co_code
# co_consts
# co_varnames
# co_names
# co_filename
# co_firstlineno
# co_lnotab
# co_freevars
# co_cellvars
# co_nlocals
# co_stacksize
# co_flags

# Compile as a module
# compile(source, filename, mode[, flags[, dont_inherit]])
# compile("x = 42", "", "exec")
# compile("42", "", "eval")
# compile("[x ** 2 for x in range(10)]", "", "exec")
# exec(compile("[x ** 2 for x in range
