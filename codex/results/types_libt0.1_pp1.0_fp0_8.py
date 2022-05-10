import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, None, class_name)

# 类方法
def func(cls):
    print('类方法')

class_name.func = classmethod(func)

# 静态方法
def func():
    print('静态方法')

class_name.func = staticmethod(func)

# 实例属性
class_name.name = '实例属性'

# 类属性
class_name.name = '类属性'

# 实例方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, None, class_
