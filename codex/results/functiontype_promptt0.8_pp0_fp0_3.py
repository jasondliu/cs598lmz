import types
# Test types.FunctionType and types.MethodType
# We create these manually because we can't access the real ones on false
assert type(lambda x: x) == types.FunctionType
assert type(lambda x: x).__name__ == 'function'
assert type(type(lambda x: x).__code__) == types.CodeType
assert type(lambda x: x).__closure__ == None
assert type(type(lambda x: x)) == types.FunctionType
class TestFunctionType(object):
    def function(self):
        pass
assert type(TestFunctionType.function) == types.FunctionType
assert type(TestFunctionType.function).__closure__ == None
assert type(TestFunctionType.function).__code__.co_freevars == ()
assert type(TestFunctionType.function).__code__.co_cellvars == ()
assert type(TestFunctionType.function).__globals__ == globals()
assert type(TestFunctionType.function).__name__ == 'function'
#assert type(TestFunctionType.function).__doc__ == None
assert type(TestFunctionType.function).__dict
