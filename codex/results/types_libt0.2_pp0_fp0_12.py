import types
types.MethodType(f, None, Student)

# 动态给类绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

# 给所有实例都绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2 = Student('Bob', 20)
s2.set_score(99)
s2.score

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添
