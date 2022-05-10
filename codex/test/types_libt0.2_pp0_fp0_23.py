import types
types.MethodType(func, None, class_name)

# 动态给类添加方法
def func(self):
    print('hello')
class_name = type('class_name', (object,), {})
class_name.func = types.MethodType(func, None, class_name)

# 动态给类添加属性
class_name = type('class_name', (object,), {})
class_name.name = 'name'

# 动态给类添加类属性
class_name = type('class_name', (object,), {})
class_name.name = 'name'

# 动态给类添加类方法
def func(cls):
    print('hello')
class_name = type('class_name', (object,), {})
