from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'my_function', None, None))


# 用元类实现单例模式
# 元类由type创建，type实际上也是一个类，它是所有类的父类
# type可以创建出类，两个参数：类名，继承的父类（元组），第三个参数是一个方法字典（可选）
# def __new__(cls, *args, **kwargs):
#     if not hasattr(cls, 'instance'):
#         cls.instance = super().__new__(cls)
#     return cls.instance
#
