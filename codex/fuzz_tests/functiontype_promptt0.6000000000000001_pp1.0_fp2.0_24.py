import types
# Test types.FunctionType

def f(): pass
def g(): pass

print isinstance(f, types.FunctionType)
print isinstance(g, types.FunctionType)

#Test types.BuiltinFunctionType

print isinstance(f, types.BuiltinFunctionType)
print isinstance(g, types.BuiltinFunctionType)

#Test types.MethodType

class C:
    def __init__(self, arg):
        pass

c = C(1)
print isinstance(c, types.MethodType)

#Test types.UnboundMethodType

print isinstance(C.__init__, types.UnboundMethodType)

#Test types.ModuleType

import sys
print isinstance(sys, types.ModuleType)

#Test types.ClassType

class D: pass

print isinstance(D, types.ClassType)

#Test types.InstanceType

print isinstance(c, types.InstanceType)

#Test types.TypeType

print isinstance(int, types.TypeType)

#Test types.TracebackType

