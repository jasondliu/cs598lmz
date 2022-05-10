import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(func=func))
class_name.func()

# 类方法
def func(cls):
    print('类方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(func=classmethod(func)))
class_name.func()

# 静态方法
def func():
    print('静态方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(func=staticmethod(func)))
class_name.func()

# 属性
class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(name='name'))
print(
