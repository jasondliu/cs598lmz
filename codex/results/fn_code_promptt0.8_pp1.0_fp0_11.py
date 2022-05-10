fn = lambda: None
# Test fn.__code__.
codefn = fn.__code__
print(codefn)
func_code_type(codefn)

# Test fn.__code__.co_code
co_code_type(codefn.co_code)

# Test fn.__code__.co_consts
co_consts_type(codefn.co_consts)

# Test fn.__code__.co_names
co_names_type(codefn.co_names)

# Test fn.__code__.co_varnames
co_varnames_type(codefn.co_varnames)

# Test fn.__code__.co_freevars
co_freevars_type(codefn.co_freevars)

# Test fn.__code__.co_cellvars
co_cellvars_type(codefn.co_cellvars)

# Test fn.__code__.co_filename
co_filename_type(codefn.co_filename)

# Test fn.__code__
