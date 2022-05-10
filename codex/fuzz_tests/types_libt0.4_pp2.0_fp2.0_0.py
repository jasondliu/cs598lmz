import types
types.MethodType(fn,obj)

# 为实例绑定方法
obj.fn = types.MethodType(fn,obj)
obj.fn()

# 为类绑定方法
Student.fn = fn
Student.fn(obj)

# 为类绑定方法
Student.fn = types.MethodType(fn,Student)
Student.fn(obj)

# 为类绑定方法
Student.fn = types.MethodType(fn,None,Student)
Student.fn(obj)

# 为类绑定方法
Student.fn = types.MethodType(fn,None,Student)
Student.fn(obj)

# 为类绑定方法
Student.fn = types.MethodType(fn,None,Student)
Student.fn(obj)

# 为类绑定方法
Student.fn =
