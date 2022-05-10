import types
# Test types.FunctionType
#
# This should be a function type.
def f():
    pass
assert type(f) is types.FunctionType
# Test types.MethodType
#
# This should be a method type.
class TestClass:
    def method(self):
        pass
assert type(TestClass().method) is types.MethodType
# Test types.BuiltinMethodType
#
# This should be a builtin method type.
assert type(TestClass.method) is types.BuiltinMethodType
# Test types.LambdaType
#
# This should be a lambda type.
assert type(lambda x: x) is types.LambdaType
# Test types.GeneratorType
#
# This should be a generator type.
def gen():
    yield 1
assert type(gen()) is types.GeneratorType
# Test types.CodeType
#
# This should be a code type.
assert type(f.__code__) is types.CodeType
# Test types.TracebackType
#
# This should be a Traceback type.
try:
    raise Exception
except:
   
