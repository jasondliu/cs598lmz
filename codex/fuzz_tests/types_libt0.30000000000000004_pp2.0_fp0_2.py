import types
types.MethodType(func, obj)

# 通过实例变量的方式绑定
obj.func = types.MethodType(func, obj)
obj.func()

# 通过类的方式绑定
Student.func = types.MethodType(func, Student)
s.func()

# 对于类的方法，只对当前类的实例有效，对其他类的实例无效
s2 = Student()
s2.func()

# 对于类的方法，只能绑定到类上，不能绑定到实例上
# s.func2 = types.MethodType(func, s)

# 对于类的方法，只能
