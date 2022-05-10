import types
# Test types.FunctionType
def f(): pass
types.FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure)
types.FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, None)
# Test types.BuiltinFunctionType
types.BuiltinFunctionType(f)
# Test types.BuiltinMethodType
types.BuiltinMethodType(f, None, None)
# Test types.UnboundMethodType
class C(object):
    def f(self): pass
types.UnboundMethodType(C.f, None, C)
# Test types.MethodType
class C(object):
    def f(self): pass
types.MethodType(C.f, None, C)
# Test types.ModuleType
types.ModuleType('__main__')
# Test types.FileType
types.FileType('f')
# Test types.TracebackType
types.TracebackType(None, None, None, None)
# Test
