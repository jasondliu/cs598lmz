import types
types.MethodType(func, obj)

# 通过实例变量的方式绑定
obj.func = types.MethodType(func, obj)
obj.func()

