import types
# Test types.FunctionType
def f():
    pass
x = types.FunctionType(f.func_code, f.func_globals, name=f.func_name,
                       argdefs=f.func_defaults, closure=f.func_closure)
assert x.func_closure == f.func_closure
assert x.func_code == f.func_code
assert x.func_defaults == f.func_defaults
assert x.func_dict == f.func_dict
assert x.func_doc == f.func_doc
assert x.func_globals == f.func_globals
assert x.func_name == f.func_name
assert x() == None
# Test types.MethodType
class C(object):
    def f(self):
        pass
assert types.MethodType(C.f, None, C)() == None
assert types.MethodType(C.f, C(), C)() == None
# Test types.UnboundMethodType
assert types.UnboundMethodType(C.f, C)() == None
# Test types.BuiltinFunction
