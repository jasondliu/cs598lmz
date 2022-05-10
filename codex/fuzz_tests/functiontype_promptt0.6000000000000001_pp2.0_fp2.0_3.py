import types
# Test types.FunctionType
def foo(): pass
assert isinstance(foo, types.FunctionType)

class A(object):
    def foo(self): pass
assert isinstance(A.foo, types.FunctionType)

# Test types.LambdaType
foo = lambda x:x
assert isinstance(foo, types.LambdaType)

# Test types.GeneratorType
def foo():
    yield 1
    yield 2
gen = foo()
assert isinstance(gen, types.GeneratorType)

# Test types.FrameType
import sys
assert isinstance(sys._getframe(), types.FrameType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.CodeType
def foo(): pass
assert isinstance(foo.func_code, types.CodeType)

# Test types.ClassType
class foo: pass
assert isinstance(foo, types.ClassType)

# Test types.InstanceType
class foo: pass

