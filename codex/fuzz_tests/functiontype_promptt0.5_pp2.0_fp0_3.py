import types
# Test types.FunctionType
if type(lambda x: x) != types.FunctionType:
    print "lambda x: x is not a FunctionType"

class C:
    def f(self): pass

# Test types.MethodType
if type(C.f) != types.MethodType:
    print "C.f is not a MethodType"

if type(C().f) != types.MethodType:
    print "C().f is not a MethodType"

if type(C.f()) != types.MethodType:
    print "C.f() is not a MethodType"

# Test types.UnboundMethodType
if type(C.f) != types.UnboundMethodType:
    print "C.f is not a UnboundMethodType"

if type(C().f) != types.UnboundMethodType:
    print "C().f is not a UnboundMethodType"

if type(C.f()) != types.UnboundMethodType:
    print "C.f() is not a UnboundMethodType"

# Test types.BuiltinFunctionType
if type(len
