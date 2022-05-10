import types
# Test types.FunctionType
@types.FunctionType
def func():
    print("this is a function")

def func2():
    print("this is a function2")
func2 = types.FunctionType(func2.__code__, func2.__globals__, name=func2.__name__,
                           argdefs=func2.__defaults__,
                           closure=func2.__closure__)

class MyType(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return {"attr": "hello"}
    def __new__(cls, name, bases, attrs):
        attrs["attr"] = "hello2"
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=MyType):
    pass

# Test types.MethodType
class C:
    def __init__(self, x):
        self.x = x

def func3(self):
    print(self.x)

c = C(2)
c.func
