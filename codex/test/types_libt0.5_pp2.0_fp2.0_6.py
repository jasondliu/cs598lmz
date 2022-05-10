import types
types.MethodType(func, obj, obj.__class__)
# 可以给一个实例绑定一个方法，但是，只对当前实例起作用，对其他实例是不起作用的

# 给实例绑定的方法，对另一个实例是不起作用的：

obj2 = Student()
obj2.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score

Student.set_score = set_score

# 通常情况下，
