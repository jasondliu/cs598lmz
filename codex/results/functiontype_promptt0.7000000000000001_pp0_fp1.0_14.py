import types
# Test types.FunctionType
def f(): pass
x = types.FunctionType(f.func_code, {})
print x
print type(x)

# Test types.InstanceType
class A(object): 
    def __init__(self):
        self.foo = 42

a = A()
i = types.InstanceType(a)
print i
print type(i)

# Test types.MethodType
class Class:
    def method(self):
        print 'method'

c = Class()
m = types.MethodType(c.method, c, Class)
print m
print type(m)

# Test types.BuiltinMethodType
print types.BuiltinMethodType(Class.method)
print type(types.BuiltinMethodType(Class.method))

# Test types.UnboundMethodType
print types.UnboundMethodType(Class.method, Class)
print type(types.UnboundMethodType(Class.method, Class))

# Test types.TracebackType
import sys
tb = types.TracebackType(sys.exc_traceback)
print
