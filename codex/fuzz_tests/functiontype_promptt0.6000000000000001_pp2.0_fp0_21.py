import types
# Test types.FunctionType
FunctionType = type(lambda: None)
# Test types.LambdaType
LambdaType = type(lambda: None)
# Test types.GeneratorType
GeneratorType = type((lambda: (yield))())


class MyClass(object):
    pass


class MyMeta(type):
    pass


class MyClass2(object, metaclass=MyMeta):
    pass


class MyClass3(MyClass, metaclass=MyMeta):
    pass


# Test types.ClassType
ClassType = type(MyClass)
# Test types.InstanceType
InstanceType = type(MyClass())
# Test types.MethodType
MethodType = type(MyClass.__init__)
# Test types.UnboundMethodType
UnboundMethodType = type(MyClass.__init__)
# Test types.BuiltinFunctionType
BuiltinFunctionType = type(len)
# Test types.BuiltinMethodType
BuiltinMethodType = type([].append)
# Test types.ModuleType
ModuleType = type(types)
# Test types.TracebackType

