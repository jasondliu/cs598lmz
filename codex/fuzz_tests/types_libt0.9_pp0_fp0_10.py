import types
types.FunctionType = (lambda: None).__class__
types.BuiltinFunctionType = type(str)
types.MethodType = types.BuiltinMethodType = (lambda: None).__str__.__class__
types.LambdaType = type(lambda: None)
types.GeneratorType = (lambda: (yield))().__class__
types.CoroutineType = type((lambda: (yield)).__await__())
types.CodeType
types.FrameType
types.TracebackType
types.GetSetDescriptorType
types.MemberDescriptorType
types.ClassMethodDescriptorType
types.WrapperDescriptorType
types.MethodWrapperType
types.StaticMethodType
types.ModuleType
types.SimpleNamespace


# -Implementation-specific-


# not exist on CPython
types.DictProxyType

# Implemented via CList on CPython and via list in Micropython
types.DequeType
types.DictItemsType
types.DictValuesType
types.MappingProxyType
types.MutableMappingType

