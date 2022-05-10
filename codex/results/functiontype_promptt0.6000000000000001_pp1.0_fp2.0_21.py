import types
# Test types.FunctionType and types.MethodType
def function1(): pass
def function2(self): pass
class C:
    def method1(self): pass
    def method2(self, arg): pass
hasattr(function1, '__call__')
isinstance(function1, types.FunctionType)
type(function1) is types.FunctionType
type(C.method1) is types.MethodType
type(C().method1) is types.MethodType
try:
    type(function2) is types.MethodType
except TypeError:
    pass
else:
    print("didn't raise TypeError")
try:
    type(C.method2) is types.MethodType
except TypeError:
    pass
else:
    print("didn't raise TypeError")
try:
    type(C().method2) is types.MethodType
except TypeError:
    pass
else:
    print("didn't raise TypeError")
