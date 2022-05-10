fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print("SKIP")
    raise SystemExit

code = fn.__code__

print(code.co_argcount)
print(code.co_nlocals)
print(code.co_stacksize)
print(code.co_flags)
print(code.co_code)
print(code.co_consts)
print(code.co_names)
print(code.co_varnames)
print(code.co_filename)
print(code.co_name)
print(code.co_firstlineno)
print(code.co_lnotab)
print(code.co_freevars)
print(code.co_cellvars)
