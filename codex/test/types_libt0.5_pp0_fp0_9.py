import types
types.MethodType(func, None)

# 方法二
from types import MethodType

def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)

# 方法三
s2 = Student('Bob')
s2.set_age(25)

# 给一个实例绑定的方法，对另一个实例是不起作用的
# 给类绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定
