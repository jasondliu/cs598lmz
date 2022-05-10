import types
# Test types.FunctionType
def f(x):
    return str(x)
if type(f) != types.FunctionType:
    print('SKIP')
    raise SystemExit

# Test types.MethodType
class C:
    def f(self, x):
        return str(x)
if type(C.f) != types.MethodType:
    print('SKIP')
    raise SystemExit

# Test types.BuiltinFunctionType
if type(len) != types.BuiltinFunctionType:
    print('SKIP')
    raise SystemExit

# Test types.BuiltinMethodType
if type(list.append) != types.BuiltinMethodType:
    print('SKIP')
    raise SystemExit

# Test types.ModuleType
if type(types) != types.ModuleType:
    print('SKIP')
    raise SystemExit

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError as e:
    if type(e.__traceback__) != types.TracebackType:
        print('SKIP')
        raise System
