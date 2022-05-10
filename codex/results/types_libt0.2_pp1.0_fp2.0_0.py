import types
types.MethodType(f, None, Student)

# 为实例绑定的方法，只对当前实例起作用，对其他实例是不起作用的
s.set_age(25)
s.age

s2 = Student()
s2.age

# 为类绑定的方法，对所有实例都起作用
Student.set_age = types.MethodType(f, Student)
s.set_age(25)
s.age
s2.set_age(25)
s2.age

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实
