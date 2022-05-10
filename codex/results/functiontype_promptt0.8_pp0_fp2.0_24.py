import types
# Test types.FunctionType
callable(types.FunctionType)

# Test types.LambdaType
callable(types.LambdaType)

# Test types.GeneratorType
callable(types.GeneratorType)

# Test types.MethodType
callable(types.MethodType)

# Test types.BuiltinFunctionType
callable(types.BuiltinFunctionType)

# Test types.BuiltinMethodType
callable(types.BuiltinMethodType)

# Test types.ModuleType
callable(types.ModuleType)

# Test types.CodeType
callable(types.CodeType)

# Test types.ClassType
class C:
    pass

C = C()
callable(types.ClassType)

# Test types.UnboundMethodType
class C:
    def f(self):
        pass

C = C()
C = C.f
callable(types.UnboundMethodType)

# Test types.InstanceType
class C:
    pass

C = C()
callable(types.InstanceType)

# Test types.
