import types
# Test types.FunctionType
class C(object):
    def f(self):
        pass
class D(object):
    pass
d = D()
d.f = types.FunctionType(C.f.im_func.func_code, {}, 'f', C.f.im_func.func_defaults, C.f.im_func.func_closure)
print d.f.im_self
print d.f()

# Test types.BuiltinFunctionType
l = []
l.append = types.BuiltinMethodType(C.f.im_func, l, list)
print l.append
