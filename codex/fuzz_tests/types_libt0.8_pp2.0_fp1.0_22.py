import types
types.MethodType(test_method,object())

#给实例绑定一个方法，对象可以调用绑定的方法
def test_method(self):
    print("test_method...")

test_obj = types.MethodType(test_method,object())
print(test_obj())

def test_method(self):
    print("test_method...")

class TestClass:
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x


'''
给类绑定方法，对象可以调用绑定的方法
'''
test_class = TestClass()
test_class.power=types.MethodType(test_method,object())
print(test_class.power())

'''
给类绑定方
