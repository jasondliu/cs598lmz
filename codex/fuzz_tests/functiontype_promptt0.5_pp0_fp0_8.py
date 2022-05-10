import types
# Test types.FunctionType
class A(object):
    def f(self):
        pass
assert isinstance(A.f, types.FunctionType)
assert isinstance(A().f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(pow, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance([].append, types.MethodType)

# Test types.MethodType
assert isinstance(A.f, types.MethodType)
assert isinstance(A().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)
assert isinstance(A().f, types.MethodType)


# Test types.TracebackType
def g():
    raise Exception
try:
    g()
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def h():

