import types
# Test types.FunctionType
def foo():pass
assert isinstance(foo, types.FunctionType)

# Test types.MethodType
class Foo:
    def bar(self):pass
assert isinstance(Foo.bar, types.MethodType)
assert isinstance(Foo().bar, types.MethodType)

# Test types.ClassType
class Foo:pass
assert isinstance(Foo, types.ClassType)

# Test types.InstanceType
f = Foo()
assert isinstance(f, types.InstanceType)

# Test types.UnboundMethodType
assert isinstance(Foo.bar, types.UnboundMethodType)

# Test types.BuiltinFunctionType
assert isinstance(foo, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(f.__str__, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try: raise Exception()
except: assert isinstance(sys.exc_info()[2], types.TracebackType
