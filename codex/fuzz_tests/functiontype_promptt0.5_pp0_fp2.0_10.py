import types
# Test types.FunctionType

def func():
    pass

class C:
    def meth(self):
        pass

    def meth2(self):
        pass

assert isinstance(func, types.FunctionType)
assert isinstance(C.meth, types.FunctionType)
assert isinstance(C.meth2, types.FunctionType)

# Test types.BuiltinFunctionType

def func():
    pass

class C:
    def meth(self):
        pass

assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(func, types.BuiltinFunctionType)
assert not isinstance(C.meth, types.BuiltinFunctionType)

# Test types.MethodType

def func():
    pass

class C:
    def meth(self):
        pass

c = C()
assert isinstance(c.meth, types.MethodType)
assert not isinstance(func, types.MethodType)
assert not isinstance(C.meth, types.MethodType)

# Test types.BuiltinMethodType

def func():
