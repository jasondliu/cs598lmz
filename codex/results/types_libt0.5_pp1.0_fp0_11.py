import types
types.MethodType(func, None, class_name)
class_name.func()

# 通过实例方法添加
class_name.func = types.MethodType(func, None, class_name)
class_name.func()

# 给对象添加方法
class_name.func = types.MethodType(func, class_name)
class_name.func()

# 实例添加方法
class_name().func = types.MethodType(func, class_name())
class_name().func()
