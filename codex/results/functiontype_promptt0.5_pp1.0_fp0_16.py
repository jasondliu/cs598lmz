import types
# Test types.FunctionType
def func():
    pass
print type(func) == types.FunctionType
print type(lambda x: x) == types.LambdaType
print type(xrange) == types.BuiltinFunctionType
print type(int) == types.BuiltinFunctionType
print type(lambda x: x) == types.FunctionType

# Test types.MethodType
class C(object):
    def meth(self):
        pass
    @classmethod
    def cmeth(cls):
        pass
    @staticmethod
    def smeth():
        pass

print type(C.meth) == types.MethodType
print type(C.cmeth) == types.MethodType
print type(C.smeth) == types.MethodType

# Test types.UnboundMethodType
print type(C.meth) == types.UnboundMethodType
print type(C.cmeth) == types.UnboundMethodType
print type(C.smeth) == types.UnboundMethodType

# Test types.BuiltinMethodType
print type(list.append) == types.BuiltinMethod
