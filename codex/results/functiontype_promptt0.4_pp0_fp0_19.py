import types
# Test types.FunctionType
def foo():
    pass
if type(foo) != types.FunctionType:
    print("Error")
# Test types.BuiltinFunctionType
try:
    if type(len) != types.BuiltinFunctionType:
        print("Error")
except NameError:
    pass
# Test types.MethodType
class A:
    def foo(self):
        pass
if type(A.foo) != types.MethodType:
    print("Error")
# Test types.UnboundMethodType
class A:
    def foo():
        pass
if type(A.foo) != types.UnboundMethodType:
    print("Error")
# Test types.BuiltinMethodType
class A:
    def foo(self):
        pass
try:
    if type(A.foo) != types.BuiltinMethodType:
        print("Error")
except NameError:
    pass
# Test types.LambdaType
if type(lambda: None) != types.LambdaType:
    print("Error")
# Test types.GeneratorType
def foo():
    yield 1

