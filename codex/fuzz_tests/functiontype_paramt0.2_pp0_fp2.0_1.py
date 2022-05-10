from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 创建类
class MyClass:
    pass

# 创建实例
obj = MyClass()

# 创建类方法
def my_method(self):
    return 'instance method called', self

# 创建类方法
from types import MethodType
obj.my_method = MethodType(my_method, obj)
obj.my_method()

# 创建类方法
MyClass.my_method = my_method
obj.my_method()

# 创建类方法
obj = MyClass()
obj.my_method()

# 创建类方法
MyClass.my_method2 = lambda self: 'lambda'
obj.my_method2()

# 创建类方法
MyClass.my_method3 = MethodType(lambda
