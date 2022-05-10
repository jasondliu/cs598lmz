fn = lambda: None
# Test fn.__code__
code = fn.__code__
print("code = fn.__code__")
print("type(code) =", type(code))
if isinstance(code, types.CodeType): print("code.co_argcount =", code.co_argcount)
print("code.co_varnames =", code.co_varnames)
print("code.co_cellvars =", code.co_cellvars)
print("code.co_freevars =", code.co_freevars)
print("code.co_filename =", code.co_filename)
print("code.co_name =", code.co_name)
print("code.co_firstlineno =", code.co_firstlineno)
print("code.co_consts =", code.co_consts)
print("code.co_names =", code.co_names)
print("code.co_varnames =", code.co_varnames)
print("code.co_stacksize =", code.co_stacksize)
print("code.co_flags
