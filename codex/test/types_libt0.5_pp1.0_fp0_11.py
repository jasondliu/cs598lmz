import types
types.MethodType(func, None, class_name)
class_name.func()

# 通过实例方法添加
class_name.func = types.MethodType(func, None, class_name)
class_name.func()
