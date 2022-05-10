import types
types.MethodType(func, None, class_name)

# 动态给实例绑定一个属性
setattr(instance, 'name', value)

# 动态给类绑定一个属性
setattr(class_name, 'name', value)

# 动态给实例绑定一个方法
setattr(instance, 'func', types.MethodType(func, instance))

# 动态给类绑定一个方法
setattr(class_name, 'func', types.MethodType(func, class_name))

# 动态给实例绑定一个类属性
setattr(instance, 'name', value)

# 动态给类绑定一个类属
