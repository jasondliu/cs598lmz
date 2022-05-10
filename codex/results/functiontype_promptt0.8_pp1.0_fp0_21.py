import types
# Test types.FunctionType
f = types.FunctionType(code, {})
if type(f) is not types.FunctionType:
    print "types.FunctionType() returned non-type"
else:
    f();
    if x != 0:
        print "types.FunctionType() returned non-function"
# Test types.MethodType
if type(c.meth) is not types.MethodType:
    print "types.MethodType() returned non-type"
else:
    c.meth()
    if x != 1:
        print "types.MethodType() returned non-method"

# types.UnboundMethodType was removed in Python 3.0
