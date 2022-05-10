from types import FunctionType
list(FunctionType(lambda:None,{}).__dict__.keys())

# 元类
# 定义元类
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('[MetaClass] __new__ called')
        return type.__new__(cls, *args, **kwargs)

# 创建类
class MyClass(metaclass=MetaClass):
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 创建实例
obj = MyClass(1, 2)

# 类属性
class MyClass:
    cls_attr = 1

# 实例属性
obj = MyClass()
obj.inst_attr = 1

# 实例方法
class MyClass:
    def inst_method(self):
        print('[inst_method] called')

