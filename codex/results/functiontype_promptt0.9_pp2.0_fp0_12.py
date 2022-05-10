import types
# Test types.FunctionType, types.MethodType.

# Create python functions.
def member_func(self): return 10;
def static_func(): return 20;

# Create python classes with these methods.
class Class:
    def member(self): return 30;
class SubClass(Class):
    def overriden_member(self): return 40;

# It is not possible to get the code object of a C++ functor.
MagicLamp = lambda : 10;

# Get python methods from python classes.
member_method = SubClass.member;
overriden_method = SubClass.overriden_member;

# These are all methods.
for method in [member_func, member_method, overriden_method, MagicLamp]:
    # These tests show that functions are not methods and vice versa.
    assert not isinstance(method, (types.FunctionType, types.MethodType)), "Method not instance of FunctionType or MethodType.";
    assert isinstance(method, (types.BuiltinFunctionType, types.BuiltinMethodType)), "Method not instance of BuiltinFunctionType or Builtin
