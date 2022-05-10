import types
types.MethodType(f, None, Student)

#给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age(25)
s.get_age()

s2 = Student()
s2.get_age()

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2.set_score(99)
s2.score

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定
