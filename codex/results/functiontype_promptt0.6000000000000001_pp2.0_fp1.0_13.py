import types
# Test types.FunctionType
def foo():
    print 'foo'

print type(foo) == types.FunctionType

# Test types.MethodType
class A(object):
    def bar(self):
        print 'A.bar'

print type(A.bar) == types.MethodType

# Test types.BuiltinMethodType
print type(len) == types.BuiltinMethodType

# Test types.UnboundMethodType
print type(A.bar) == types.UnboundMethodType

# Test types.InstanceType
a = A()
print type(a) == types.InstanceType

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    import sys
    tb = sys.exc_info()[2]
    print type(tb) == types.TracebackType

# Test types.FrameType
def baz():
    print type(sys._getframe()) == types.FrameType

baz()

# Test types.CodeType
def qux(): pass
print type(qux.func_code) == types
