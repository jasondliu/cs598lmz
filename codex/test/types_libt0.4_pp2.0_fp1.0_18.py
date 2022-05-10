import types
types.MethodType(func, obj)

# 给实例绑定的方法，只对该实例起作用，对其他实例是不起作用的

# 为了给所有实例都绑定方法，可以给class绑定方法

Student.set_score = types.MethodType(set_score, Student)

s.set_score(100)

# 给class绑定方法后，所有实例均可调用

s2 = Student()
s2.set_score(99)

