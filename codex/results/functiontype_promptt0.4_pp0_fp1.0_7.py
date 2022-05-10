import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f()) is types.NoneType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType
assert type(lambda x, y: x) is types.FunctionType
assert type(lambda x, y=42: x) is types.FunctionType
assert type(lambda *args: args) is types.FunctionType
assert type(lambda **kw: kw) is types.FunctionType
assert type(lambda *args, **kw: args) is types.FunctionType
assert type(lambda *args, **kw: kw) is types.FunctionType
assert type(lambda *args, **kw: (args, kw)) is types.FunctionType
assert type(lambda x=None, y=None: (x, y)) is types.FunctionType

# Test types.MethodType
class C(object):
    def meth(self): pass
assert type(C.meth) is types.MethodType
assert type(C.meth(C())) is types.NoneType

