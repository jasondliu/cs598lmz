import types
# Test types.FunctionType, types.LambdaType and types.ClassType

f = lambda: 10
print type(f)

def ff(): pass
print type(ff)

class A: pass
a = A()
print type(a)

# Test types.MethodType

class B:
    def bf(self): pass

b = B()
print type(b.bf)

# Test types.UnboundMethodType

print type(B.bf)

# Test types.BuiltinFunctionType

print type(open)
print type(str)

# Test types.BuiltinMethodType

print type([].append)
print type(''.join)
print type(object.__new__)

# Test types.InstanceType

class C: pass
c = C()
print type(c)

# Test types.NoneType

n = None
print type(n)

# Test types.TracebackType
def tracer(frame, event, arg):
    pass
import sys
tb = sys.settrace(tracer)
print type(t
