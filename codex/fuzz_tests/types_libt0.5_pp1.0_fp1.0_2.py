import types
types.MethodType(f, str)

# 为实例绑定的方法，对另一个实例是不起作用的
s1 = Student()
s2 = Student()
s1.set_age(25)
s1.set_age(25)
# s2.set_age(25)

# 给一个实例绑定的方法，对另一个实例是不起作用的，
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print s.score
s2.set_score(99)
print s2.score

#
