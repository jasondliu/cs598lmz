import types
# Test types.FunctionType
assert(isinstance(foo, types.FunctionType))

def foo(x):
    return x + 42

# Test types.LambdaType
l = lambda x: x + 42
assert(isinstance(l, types.LambdaType))

import types
# Test types.GeneratorType
def foo():
    yield 42

g = foo()
assert(isinstance(g, types.GeneratorType))

# Test types.CodeType
def foo(x):
    return x + 42
assert(isinstance(foo.__code__, types.CodeType))

import types
# Test types.FrameType
def foo():
    return 42

assert(isinstance(foo.__code__.__frame__, types.FrameType))

# Test types.TracebackType
import sys
def foo():
    return sys.exc_info()[2]

assert(isinstance(foo(), types.TracebackType))

# Test types.GetSetDescriptorType
class Foo(object):
    def getx(self): return self.__x

