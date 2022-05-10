import types
# Test types.FunctionType with the *args syntax.
def dummy_func(*args):
    pass

types.FunctionType(dummy_func.func_code, dummy_func.func_globals)

# Test types.FunctionType with the **kwds syntax.
def dummy_func(**kwds):
    pass

types.FunctionType(dummy_func.func_code, dummy_func.func_globals)

# Test types.FunctionType with both *args and **kwds.
def dummy_func(*args, **kwds):
    pass

types.FunctionType(dummy_func.func_code, dummy_func.func_globals)

# Test types.FunctionType with an invalid first arg.
try:
    types.FunctionType((1,2), dummy_func.func_globals)
except TypeError:
    pass
else:
    print "types.FunctionType accepted a non-code object as the first arg"

# Test types.FunctionType with an invalid second arg.
try:
    types.FunctionType(dummy_func.func_code
