import types
# Test types.FunctionType
def f():
    pass

isinstance(f, types.FunctionType)

# Internal types are not exported
try:
    isinstance(f, types._FunctionType)
except AttributeError:
    pass
else:
    assert False, 'should raise AttributeError'

# Subclassing internal types does not work
try:
    class C(types._FunctionType):
        pass
except TypeError:
    pass
else:
    assert False, 'should raise TypeError'

# But instance of internal type can be used to check
isinstance(f, types._FunctionType())

# Test types.MethodType
class C:
    def f(self):
        pass

isinstance(C.f, types.MethodType)

# Internal types are not exported
try:
    isinstance(C.f, types._MethodType)
except AttributeError:
    pass
else:
    assert False, 'should raise AttributeError'

# Subclassing internal types does not work
try:
    class C(types._MethodType):
        pass
except TypeError
