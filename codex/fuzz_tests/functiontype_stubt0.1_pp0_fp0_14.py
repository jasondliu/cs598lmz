from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)
print(type(a.__next__) == types.BuiltinFunctionType)
print(type(a.__next__) == types.MethodType)
print(type(a.__next__) == types.BuiltinMethodType)
print(type(a.__next__) == types.MethodDescriptorType)
print(type(a.__next__) == types.MemberDescriptorType)
print(type(a.__next__) == types.GetSetDescriptorType)
print(type(a.__next__) == types.WrapperDescriptorType)
print(type(a.__next__) == types.MethodWrapperType)
print(type(a.__next__) == types.MethodWrapperDescriptorType)
print(type(a.__next__) == types.ClassMethod
