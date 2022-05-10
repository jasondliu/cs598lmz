import types
types.ModuleType

# 创建一个类
class MyClass:
    pass

# 创建一个实例
my_class = MyClass()

# 创建一个类
class MyClass:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 创建一个实例
my_class = MyClass('张三', 18)

# 访问实例属性
my_class.name
my_class.age

# 创建一个类
class MyClass:
    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def say_hello(self):
        print
