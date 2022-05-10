import types
types.MethodType(new_func, obj)

# 给实例绑定的方法，对另一个实例是不起作用的
obj2 = Student()
# obj2.set_age(25)

# 给类绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
obj.set_score(100)
print(obj.score)
obj2.set_score(99)
print(obj2.score)

# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这
