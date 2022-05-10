import types
# Test types.FunctionType
#class TestFake:
#    pass
#assert type(TestFake.fake) == types.FunctionType
# Test types.BuiltinFunctionType
# Test the comment is a part of the builtin function type too :P
#assert type(dir) == types.BuiltinFunctionType
def Testf:
    pass
# Test types.MethodType
assert type(Testf.__get__) == types.MethodType
class MyInt:
    def __int__(self):
        return 0
# Test types.UnboundMethodType
assert type(MyInt.__int__) == types.UnboundMethodType
assert type(MyInt().__int__) == types.MethodType
# Test types.LambdaType
assert type((lambda x: x)(0)) == types.LambdaType
# Test types.GeneratorType
def makeGenerator():
    for n in xrange(5):
        yield n
assert type(makeGenerator()) == types.GeneratorType
# Test types.CodeType
#assert type(makeGenerator.func_code) == types.CodeType
assert type(
