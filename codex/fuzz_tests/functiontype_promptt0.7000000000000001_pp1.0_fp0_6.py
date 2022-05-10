import types
# Test types.FunctionType
x = types.FunctionType(types.CodeType(0, 0, 0, 0, 0, b"", (), (), (), "", "", 0, b""), {})
# Test types.BuiltinFunctionType
import os
x = types.BuiltinFunctionType(os._exit, {})
# Test types.BuiltinMethodType
class C:
    @staticmethod
    def f(): pass
x = types.BuiltinMethodType(C.f, None, C)
# Test types.LambdaType
x = types.LambdaType(types.CodeType(0, 0, 0, 0, 0, b"", (), (), (), "", "", 0, b""), {})
# Test types.MethodType
class C:
    @staticmethod
    def f(): pass
x = types.MethodType(C.f, None)
# Test types.UnboundMethodType
class C:
    @staticmethod
    def f(): pass
x = types.UnboundMethodType(C.f, None, C)
# Test types.ModuleType
x = types.ModuleType("hello
