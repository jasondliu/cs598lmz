import types
types.MethodType(func, None, class_name)

# 动态给实例绑定一个属性
setattr(instance, 'name', value)

# 动态给类绑定一个属性
setattr(class_name, 'name', value)

# 动态给类绑定一个方法
setattr(class_name, 'func', func)

# 动态给实例绑定一个方法
setattr(instance, 'func', func)

