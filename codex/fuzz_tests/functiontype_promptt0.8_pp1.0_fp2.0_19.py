import types
# Test types.FunctionType
def f(): pass
if type(f) != types.FunctionType:
    raise TestFailed, "expected types.FunctionType"
# Test types.ClassType
c = type(types)
if c != types.ClassType:
    raise TestFailed, "expected types.ClassType"
# Test types.UnboundMethodType
# XXX
# print "XXX test UnboundMethodType"
# f = types.UnboundMethodType
# if type(f) != types.UnboundMethodType:
#     raise TestFailed, "expected types.UnboundMethodType"
# Test types.MethodType
f = c.__dict__['__name__']
if type(f) != type(type.__dict__):
    raise TestFailed, "expected types.MethodType"

# Test try/except/else
try:
    pass
except:
    raise TestFailed, "try/except/else"
else:
    pass

# Test try/finally
try:
    pass
finally:
    pass

# Test yield
# XXX
# print "XXX test
