import types
# Test types.FunctionType
def test_type_functiontype():
    def x():
        pass
    assert isinstance(x, types.FunctionType)

# Test types.LambdaType
def test_type_lambdatype():
    assert isinstance(lambda: None, types.LambdaType)

# Test types.UnboundMethodType
def test_type_unboundmethodtype():
    class C:
        def x(): pass
    assert isinstance(C.x, types.UnboundMethodType)

# Test type.BuiltinMethodType
import sys
dir(sys)
class C: pass
assert isinstance(dir, types.BuiltinFunctionType)
assert isinstance(C.__add__, types.BuiltinMethodType)


# Test types.GeneratorType
def test_type_generatortype():
    def hello():
        for i in range(5):
            yield str(i)
    assert isinstance(hello(), types.GeneratorType)

# Test types.CodeType

import types
assert types.CodeType(0,0,0,0,"","
