import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name = types.new_class('class_name', (), {'func': func})
instance = class_name()
instance.func()

# 类方法
def func(cls):
    print('类方法')

class_name = types.new_class('class_name', (), {'func': classmethod(func)})
class_name.func()

# 静态方法
def func():
    print('静态方法')

class_name = types.new_class('class_name', (), {'func': staticmethod(func)})
class_name.func()

# 属性
class_name = types.new_class('class_name', (), {'name': 'name'})
instance = class_name()
print(instance.name)

# 类属
