import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(f.__call__, types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass

a = A()
assert isinstance(a.f, types.MethodType)
assert isinstance(a.f, types.BuiltinMethodType)

# Test types.GeneratorType
def f():
    yield 1

g = f()
assert isinstance(g, types.GeneratorType)

# Test types.FrameType
def f():
    return sys._getframe()

frame = f()
assert isinstance(frame, types.FrameType)

# Test types.GetSetDescriptorType
class A(object):
    def __get__(self, obj, objtype):
        return "A"

class B(object):
    a = A()

assert isinstance(B.a
