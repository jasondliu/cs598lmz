import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass
def i(): pass

t = types.FunctionType(f.func_code, f.func_globals)
print t.func_code == f.func_code
print t.func_globals == f.func_globals

# Test types.MethodType
class C:
    def m(self): pass
    def n(self): pass
    def o(self): pass
    def p(self): pass

c = C()

t = types.MethodType(c.m.im_func, c, c.__class__)
print t.im_func == c.m.im_func
print t.im_self == c
print t.im_class == c.__class__

# Test types.BuiltinFunctionType
t = types.BuiltinFunctionType(range)
print t.__name__ == 'range'

# Test types.BuiltinMethodType
t = types.BuiltinMethodType(c.m.im_func, c, c.__class__)

