import types
# Test types.FunctionType
def func():
    pass
print "function" if isinstance(func, types.FunctionType) else "not function"

# Test types.LambdaType
lambdaFunc = lambda x: True
print "function" if isinstance(lambdaFunc, types.LambdaType) else "not function" # True, "function"

# Test types.BuiltinFunctionType
print "function" if isinstance(print, types.BuiltinFunctionType) else "not function"

# Test types.MethodType
class A:
    def func(self):
        pass
inst = A()
print "function" if isinstance(inst.func, types.MethodType) else "not function"
