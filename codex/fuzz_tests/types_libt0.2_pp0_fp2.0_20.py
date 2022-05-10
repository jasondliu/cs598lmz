import types
types.MethodType(lambda self: self.name, None, Person)

# 给实例绑定的方法，对另一个实例是不起作用的
p1.set_age(25)
p1.get_age()
p2.get_age()

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Person.set_score = set_score

p1.set_score(100)
p1.score
p2.set_score(99)
p2.score

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允
