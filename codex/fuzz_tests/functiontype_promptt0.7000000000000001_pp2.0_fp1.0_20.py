import types
# Test types.FunctionType
try:
    types.FunctionType
except AttributeError:
    print('SKIP')
    raise SystemExit

def f(a, b, c=1, d=2, *args, **kwargs):
    pass

# Test types.CodeType
try:
    types.CodeType
except AttributeError:
    print('SKIP')
    raise SystemExit

code = f.__code__
print(code.co_filename)
print(code.co_name)
print(code.co_argcount)
print(code.co_kwonlyargcount)
print(code.co_nlocals)
print(code.co_stacksize)
print(code.co_flags)
print(code.co_code)
print(code.co_consts)
print(code.co_names)
print(code.co_varnames)
print(code.co_freevars)
print(code.co_cellvars)
print(code.co_firstlineno)
print(code.co_lnotab)
print(
