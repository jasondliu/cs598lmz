import types
types.MethodType(f, None, Student)

# 给实例绑定一个方法
s.set_age = MethodType(f, s)
