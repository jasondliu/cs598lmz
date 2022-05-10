import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

# Test types.CodeType
def f(): pass
assert type(f.__code__) is types.CodeType

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
assert type(f()) is types.FrameType

# Test types.TracebackType
def g():
    1/0
def f():
    try:
        g()
    except ZeroDivisionError:
        import sys
        return sys.exc_info()[2]
assert type(f()) is types.TracebackType

# Test types.ModuleType
assert type(types) is types.ModuleType

# Test types.MethodType
class C:
    def
