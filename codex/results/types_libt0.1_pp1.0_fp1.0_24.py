import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name = types.MethodType(func, None, class_name)

# 类方法
def func(cls):
    print('类方法')

class_name = types.MethodType(func, class_name)

# 静态方法
def func():
    print('静态方法')

class_name = types.MethodType(func, class_name)

# 实例属性
class_name.name = '实例属性'

# 类属性
class_name.age = '类属性'

# 实例方法
class_name.func = func

# 类方法
class_name.func2 = classmethod(func)


