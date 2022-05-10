import types
# Test types.FunctionType
print type(len)
print type(int)
print type(lambda x: x)
# Test types.LambdaType
print type(lambda x: x)
# Test types.GeneratorType
def testGenerator():
    yield 1
print type(testGenerator())
# Test types.ClassType and types.InstanceType
class TestClass():
    pass
print type(TestClass)
print type(TestClass())
# Test types.TypeType
#print type(types)
# Test types.UnboundMethodType
class UnboundClass():
    def unboundMethod(self, x):
        return x + 1
print type(UnboundClass.unboundMethod)
# Test types.MethodType
class MethodClass():
    def method(self):
        pass
class InheritedMethodClass(MethodClass):
    pass
print type(MethodClass.method)
print type(MethodClass().method)
print type(InheritedMethodClass.method)
print type(InheritedMethodClass().method)
# Test CPython specific types
import sys
if sys.platform == "cli":
   
