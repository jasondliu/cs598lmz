import types
# Test types.FunctionType
try:
    def f(*args, **kwargs):
        return args, kwargs
    assert type(f) is types.FunctionType
except Exception as e:
    print('Error:', e)

# Test types.LambdaType
try:
    f = lambda x: x
    assert type(f) is types.LambdaType
except Exception as e:
    print('Error:', e)

# Test types.BuiltinFunctionType
try:
    assert type(len) is types.BuiltinFunctionType
except Exception as e:
    print('Error:', e)

# Test types.MethodType
try:
    class C:
        def f(self):
            pass
    assert type(C().f) is types.MethodType
except Exception as e:
    print('Error:', e)

# Test types.GeneratorType
try:
    def f():
        yield 1
    assert type(f()) is types.GeneratorType
except Exception as e:
    print('Error:', e)

# Test types.ClassType
try
