import types
# Test types.FunctionType
def function():
    print "function"

def test_function_type():
    assert type(function) == types.FunctionType

# Test types.LambdaType
test_lambda_type = lambda: "lambda"
assert type(test_lambda_type) == types.LambdaType

# Test types.GeneratorType
def generator():
    yield 1
    yield 2

def test_generator_type():
    assert type(generator()) == types.GeneratorType

# Test types.CodeType
def test_code_type():
    assert type(function.func_code) == types.CodeType

# Test types.TypeType
def test_type_type():
    assert type(int) == types.TypeType

# Test types.ClassType
class TestClass:
    pass

def test_class_type():
    assert type(TestClass) == types.ClassType

# Test types.UnboundMethodType
class TestUnboundMethod:
    def method():
        pass

def test_unbound_method_type():
    assert type(
