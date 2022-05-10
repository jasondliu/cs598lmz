import types
types.MethodType(f,None,class_name)

#给一个实例绑定的方法，对另一个实例是不起作用的
s.set_age(25)
s.get_age()

s2 = Student()
s2.get_age()

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2.set_score(99)
s2.score

#使用__slots__
#如果我们想要限制实例的属性怎么办？比如，只
