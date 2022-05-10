import types
types.MethodType(func, None, class_name)

# 实例方法
def func(self):
    print('实例方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(dict(func=func)))
types.MethodType(func, class_name())

# 类方法
def func(cls):
    print('类方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(dict(func=func)))
types.MethodType(func, class_name)

# 静态方法
def func():
    print('静态方法')

class_name = types.new_class('class_name', (), {}, lambda ns: ns.update(dict(func=func)))
class_name.func = func

# 属性
