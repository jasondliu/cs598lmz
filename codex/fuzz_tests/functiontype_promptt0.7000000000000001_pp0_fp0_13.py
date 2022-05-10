import types
# Test types.FunctionType

def f():
    pass

print isinstance(f, types.FunctionType)
print isinstance(f, types.MethodType)
# Test types.MethodType

class A(object):
    def method(self):
        pass

print isinstance(A.method, types.MethodType)
print isinstance(A.method, types.FunctionType)
# Test types.LambdaType

print isinstance(lambda x:x, types.LambdaType)
# Test types.GeneratorType

print isinstance((i for i in range(10)), types.GeneratorType)
print isinstance([], types.GeneratorType)
# Test types.SliceType
print isinstance(slice(1,2,3), types.SliceType)
print isinstance([1,2,3], types.SliceType)
# Test types.EllipsisType

print isinstance(Ellipsis, types.EllipsisType)
print isinstance(1, types.EllipsisType)
# Test types.TracebackType

import sys
print isinstance(
