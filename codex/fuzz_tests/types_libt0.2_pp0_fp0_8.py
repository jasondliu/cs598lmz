import types
types.MethodType(f, None, Student)

# 为实例绑定的方法，只对当前实例起作用，对其他实例无效
s.set_age(25)
s.age

s2 = Student()
s2.age

# 为类绑定方法，对所有实例起作用
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2.set_score(99)
s2.score

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允
