import types
# Test types.FunctionType
def func(): pass
TEST(type(func) == types.FunctionType)
TEST(type(func) is types.FunctionType)
TEST(isinstance(func, types.FunctionType))
TEST(not issubclass(types.FunctionType, object))

# Test types.MethodType
def func_with_self(self): pass
class C: pass
c = C()
c.f = func_with_self
TEST(type(func_with_self) is types.FunctionType)
TEST(not isinstance(func_with_self, types.MethodType))
TEST(not issubclass(types.MethodType, object))

TEST(type(c.f) is types.MethodType)
TEST(isinstance(func_with_self, types.FunctionType))
TEST(not issubclass(types.MethodType, object))

# Test types.BuiltinFunctionType
TEST(type(print) is types.BuiltinFunctionType)
TEST(isinstance(print, types.BuiltinFunctionType))
TEST(not issub
