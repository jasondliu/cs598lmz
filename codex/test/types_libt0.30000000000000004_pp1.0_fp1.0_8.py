import types
types.MethodType(func, None, class_name)

# 要给所有实例都绑定方法，可以给class绑定方法：
class_name.func = func
