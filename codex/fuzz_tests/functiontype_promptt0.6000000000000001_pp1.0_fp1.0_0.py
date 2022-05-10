import types
# Test types.FunctionType and types.MethodType
#

# Test a function
def func():
    pass

if type(func) != types.FunctionType:
    raise TestFailed, "type(func) is not types.FunctionType"

# Test a method
class C:
    def meth(self):
        pass

if type(C.meth) != types.MethodType:
    raise TestFailed, "type(C.meth) is not types.MethodType"

# Test a method with a weird name
class D:
    def __call__(self):
        pass

if type(D().__call__) != types.MethodType:
    raise TestFailed, "type(D().__call__) is not types.MethodType"

# Test a built-in method
if type(str.split) != types.MethodType:
    raise TestFailed, "type(str.split) is not types.MethodType"

# Test a built-in function
if type(map) != types.BuiltinFunctionType:
    raise TestFailed, "type(map)
