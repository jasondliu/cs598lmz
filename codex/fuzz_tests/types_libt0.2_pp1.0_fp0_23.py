import types
types.MethodType(f, None, Student)

# 为实例绑定一个方法
s.set_age = MethodType(f, s)
s.set_age(25)
s.age

# 为类绑定方法
Student.set_score = MethodType(f, None, Student)
s.set_score(100)
s.score

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__
