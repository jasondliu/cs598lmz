import types
# Test types.FunctionType
def f(): pass
print type(f)

# Test types.LambdaType
g = lambda: None
print type(g)

# Test types.GeneratorType
def h(): yield None
print type(h())

# Test types.BuiltinFunctionType
print type(len)

# Test types.BuiltinMethodType
print type([].append)

# Test types.MethodType
class A(object):
    def f(self): pass
print type(A().f)

# Test types.UnboundMethodType
print type(A.f)

# Test types.InstanceType
class B(object): pass
b = B()
print type(b)

# Test types.ClassType
class C: pass
print type(C)

# Test types.TypeType
print type(type)

# Test types.FileType
import sys
print type(sys.stdin)

# Test types.XRangeType
print type(xrange(0))

# Test types.SliceType
print type(slice(0))

# Test types.
