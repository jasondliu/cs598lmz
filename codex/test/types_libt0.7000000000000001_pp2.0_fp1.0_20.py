import types
types.MethodType(func,obj)

# 为对象绑定一个方法
obj.fun = types.MethodType(func,obj)
obj.fun()
