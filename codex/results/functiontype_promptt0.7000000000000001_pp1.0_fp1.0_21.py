import types
# Test types.FunctionType
try:
    f = types.FunctionType
except AttributeError:
    raise ImportError

try:
    f = types.FunctionType(f.func_code, f.func_globals, 'foo', f.func_defaults)
except:
    print 'Failed to create function object'
    raise

if f.func_name != 'foo':
    print 'Wrong func_name attribute'

if f.func_code is None:
    print 'Wrong func_code attribute'

if f.func_globals is None:
    print 'Wrong func_globals attribute'

if f.func_defaults is not None:
    print 'Wrong func_defaults attribute'

try:
    f = types.FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure)
except:
    print 'Failed to create function object'
    raise

if f.func_defaults is not None:
    print 'Wrong func
