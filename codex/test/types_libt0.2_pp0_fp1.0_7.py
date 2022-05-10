import types
types.MethodType(f, None, Student)

# 为实例绑定一个方法
s.set_age = MethodType(f, s)
s.set_age(25)
s.age

# 为类绑定方法
Student.set_score = MethodType(f, None, Student)
