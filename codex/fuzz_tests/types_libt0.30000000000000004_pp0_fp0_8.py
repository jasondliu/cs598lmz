import types
types.MethodType(f, None, class_name)

# 动态给实例绑定一个属性
class_name.name = 'lisi'
print(class_name.name)

# 动态给实例绑定一个方法
class_name.f = types.MethodType(f, class_name)
class_name.f()

# 动态给类绑定一个属性
class_name.age = 18
print(class_name.age)

# 动态给类绑定一个方法
class_name.f = types.MethodType(f, class_name)
class_name.f()

# 动态给类绑定一个方法
def f(self):
    print('给类绑定一个
