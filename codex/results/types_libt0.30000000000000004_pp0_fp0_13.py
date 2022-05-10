import types
types.MethodType(func, None, class_name)

# 实例方法
class_name.func = types.MethodType(func, None, class_name)

# 类方法
class_name.func = classmethod(func)

# 静态方法
class_name.func = staticmethod(func)

# 属性
class_name.attr = value

# 实例属性
class_name.attr = value

# 类属性
class_name.attr = value

# 删除方法
del class_name.func

# 删除属性
del class_name.attr

# 删除实例属性
del class_name.attr

# 删除类属性
del class_name.attr

# 删除类
del class_name

#
