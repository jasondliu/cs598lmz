import types
# Test types.FunctionType
@types.FunctionType
def f():
    pass
class Foo:
    @types.FunctionType
    def f(self):
        pass
# Test types.BuiltinFunctionType
# - This can't actually be tested, because the JVM
#   doesn't expose a builtin function type. Using this
#   on a CPython function raises a class cast exception
#   on the JVM.
# Test types.MethodType
def f():
    pass
class Foo:
    pass
m = types.MethodType(f, Foo)
# Test types.TracebackType
# - Not implemented
# Test types.FrameType
# - Not implemented
