import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, class_name)

# 类方法
def func(cls):
    print('类方法')

class_name.func = classmethod(func)

# 静态方法
def func():
    print('静态方法')

class_name.func = staticmethod(func)

# 删除方法
del class_name.func

# 删除属性
del class_name.name

# 删除实例
del class_name

# 删除类
del class_name

# 删除模块
del sys

# 删除内置函数

