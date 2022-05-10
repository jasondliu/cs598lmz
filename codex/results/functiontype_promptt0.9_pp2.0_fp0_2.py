import types
# Test types.FunctionType()
try:
    import types
    try:
        res = types.FunctionType
    except:
        print('SKIP')
        raise SystemExit
except ImportError:
    print('SKIP')
    raise SystemExit

print(types.MethodType(res, 1))
print(types.ModuleType(res))
print(types.ClassType(res))
