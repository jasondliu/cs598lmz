import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name = types.MethodType(func, None)

# 类方法
def func(cls):
    print('类方法')

class_name = types.MethodType(func, None, class_name)

# 静态方法
def func():
    print('静态方法')

class_name = types.MethodType(func, None, class_name)

