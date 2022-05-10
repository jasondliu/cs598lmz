fn = lambda: None
# Test fn.__code__
print(fn.__code__)

import types
# Test types.CodeType
code = fn.__code__
print(type(code))
# Test from_code
print(types.CodeType.from_code(code))
# Test from_canonical
print(types.CodeType.from_canonical(code))

# Test types.FrameType
# This is a read-only view of a different object.
import sys
print(type(sys._getframe()))

# Test types.FunctionType
print(type(fn))
# Test types.GeneratorType
def coro():
    yield 1
print(type(coro()))

# Test types.GetSetDescriptorType
class Foo:
    @property
    def prop(self):
        return 42
    @prop.setter
    def prop(self, value):
        pass

print(type(Foo.prop))

# Test types.LambdaType
a_lambda = lambda: None
print(type(a_lambda))

# Test types.MappingProxyType
frozen
